# Generated by Django 4.0.2 on 2022-02-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantprofile',
            name='menu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', related_query_name='restaurant', to='Restaurants.menu'),
        ),
    ]
