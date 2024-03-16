from django.db import models

class ConnectorType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ChargingStation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    pricing = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    distance = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # Add distance field
      # Add balance field


    def __str__(self):
        return self.name


class Connector(models.Model):
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE, related_name='connectors')
    connector_type = models.ForeignKey(ConnectorType, on_delete=models.CASCADE)
    current_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.charging_station.name} - {self.connector_type.name}"
    

