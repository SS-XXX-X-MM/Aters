# Generated by Django 4.0.2 on 2022-02-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_address_locality_alter_address_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
