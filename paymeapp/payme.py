import requests
import json
import time


class Payme:
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "uz,en;q=0.9,ru;q=0.8",
        "app-theme": "light",
        "app-version": "10.84.1460",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Yandex\";v=\"23\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-accept-language": "ru",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    card_id = "63cfa6e8f9b3d2b5a8fe0fb2"
    create_url = "https://payme.uz/api/p2p.create"
    check_url = "https://payme.uz/api/cheque.get"

    def create(self, amount):
        try:
            amount *= 100
            data = json.dumps({"method": "p2p.create", "params": {"card_id": self.card_id, "amount": amount}})
            res = requests.post(url=self.create_url, data=data, headers=self.headers).json()
            try:
                pay_id = res["result"]["cheque"]["_id"]
                res['pay_id'] = pay_id
                res['pay_url'] = f"https://checkout.paycom.uz/{pay_id}"
                return res
            except:
                return res
        except:
            return {"res": "payme.system.error"}

    def check(self, id):
        try:
            data = json.dumps({"method": "cheque.get", "params": {"id": id}})
            res = requests.post(url=self.check_url, data=data, headers=self.headers).json()
            pay_time = res['result']['cheque']['pay_time']

            if pay_time == 0:
                return False
            else:
                return True
        except:
            return False
