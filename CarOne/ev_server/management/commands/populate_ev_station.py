import random
from django.core.management.base import BaseCommand
from ev_server.models import ChargingStation, ConnectorType, Connector

class Command(BaseCommand):
    help = 'Populate charging stations and connectors'

    def handle(self, *args, **kwargs):
        # Assuming you have the data of EV stations as a list of dictionaries
        ev_stations_data = [
    {
        'name': 'Station A',
        'latitude': 40.7128,
        'longitude': -74.0060,
        'pricing': 0.15,  # Price per kWh
        'balance': 500.0,  # Initial balance
        'distance':50
    },
    {
        'name': 'Station B',
        'latitude': 34.0522,
        'longitude': -118.2437,
        'pricing': 0.20,
        'balance': 300.0,
        'distance':60.02
    },
    {
        'name': 'Station C',
        'latitude': 51.5074,
        'longitude': -0.1278,
        'pricing': 0.18,
        'balance': 700.0,
        'distance':20.00
    },
    # Add more stations as needed
]

        # Populate charging stations
        for station_data in ev_stations_data:
            station = ChargingStation.objects.create(
                name=station_data['name'],
                latitude=station_data['latitude'],
                longitude=station_data['longitude'],
                pricing=station_data['pricing'],
                balance=station_data['balance'],
                distance=station_data['distance']
            )

            # Add connectors
            connector_types = ConnectorType.objects.all()
            for _ in range(2):  # Add 2 connectors for each station
                connector_type = random.choice(connector_types)
                max_charging_power = random.uniform(10.0, 50.0)  # Example range for max charging power
                current_status = random.choice(['Available', 'Occupied', 'Under Management'])
                Connector.objects.create(
                    charging_station=station,
                    connector_type=connector_type,
                    current_status=current_status
                )

        self.stdout.write(self.style.SUCCESS('Charging stations and connectors populated successfully.'))