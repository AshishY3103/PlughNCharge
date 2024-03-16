# Generated by Django 5.0.2 on 2024-03-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ev_server', '0002_remove_chargingstation_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='chargingstation',
            name='pricing',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=11),
        ),
    ]