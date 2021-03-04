# Generated by Django 3.1.6 on 2021-02-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengers',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flight.Flight'),
        ),
    ]
