# Generated by Django 4.1.7 on 2023-02-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_alter_ordermodel_user_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='gmail',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]
