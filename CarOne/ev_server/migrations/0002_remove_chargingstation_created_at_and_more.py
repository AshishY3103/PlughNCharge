# Generated by Django 5.0.2 on 2024-03-15 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ev_server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chargingstation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='chargingstation',
            name='pricing',
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_charging_power', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current_status', models.CharField(max_length=50)),
                ('charging_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectors', to='ev_server.chargingstation')),
                ('connector_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ev_server.connectortype')),
            ],
        ),
        migrations.DeleteModel(
            name='ChargingStationConnector',
        ),
    ]