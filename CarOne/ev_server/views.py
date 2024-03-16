from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from ev_server.models import ConnectorType,ChargingStation,Connector



def upd(request):


    # Create charging stations
        station_a = ChargingStation.objects.create(name="Station D", latitude=37.7749, longitude=-122.4194)
        station_b = ChargingStation.objects.create(name="Station E", latitude=37.7745, longitude=-122.4188)
        station_c = ChargingStation.objects.create(name="Station F", latitude=37.7735, longitude=-122.4172)


        avilability_values =['Available','Occupied']

        
