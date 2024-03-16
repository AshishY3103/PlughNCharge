from django.contrib import admin
from .models import ConnectorType,ChargingStation,Connector

my_models = [ConnectorType,ChargingStation,Connector]
for model in my_models:
    admin.site.register(model)
