# Generated by Django 4.0.2 on 2022-02-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_address_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='locality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100),
        ),
    ]
