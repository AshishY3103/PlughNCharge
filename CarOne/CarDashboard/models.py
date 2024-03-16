from django.db import models

class EVUser(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    battery_status = models.DecimalField(max_digits=5, decimal_places=2)  # Represented as percentage
    charger_type = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_registered = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Add balance field

    def __str__(self):
        return self.name

