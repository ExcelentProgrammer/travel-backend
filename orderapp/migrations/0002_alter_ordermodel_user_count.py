# Generated by Django 4.1.7 on 2023-02-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='user_count',
            field=models.IntegerField(default=1),
        ),
    ]
