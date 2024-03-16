from django.core.management.base import BaseCommand
from CarDashboard.models import EVUser
import json

class Command(BaseCommand):
    help = 'Insert sample EV user data into the database'

    def handle(self, *args, **kwargs):
        # Sample EV user data
        ev_users_data = [
            {
                "name": "John Doe",
                "address": "123 Main St, Anytown, USA",
                "battery_status": 80.0,
                "charger_type": "Type 2",
                "email": "john.doe@example.com",
                "phone_number": "+1234567890",
                "date_registered": "2024-03-14T12:00:00Z"
            },
            {
                "name": "Alice Smith",
                "address": "456 Elm St, Othertown, USA",
                "battery_status": 65.5,
                "charger_type": "CHAdeMO",
                "email": "alice.smith@example.com",
                "phone_number": "+1987654321",
                "date_registered": "2024-03-15T10:30:00Z"
            },
            {
                "name": "Bob Johnson",
                "address": "789 Oak St, Anycity, USA",
                "battery_status": 90.0,
                "charger_type": "CCS",
                "email": "bob.johnson@example.com",
                "phone_number": "+1122334455",
                "date_registered": "2024-03-16T09:15:00Z"
            }
        ]

        # Insert EV user data into the database
        for user_data in ev_users_data:
            EVUser.objects.create(
                name=user_data["name"],
                address=user_data["address"],
                battery_status=user_data["battery_status"],
                charger_type=user_data["charger_type"],
                email=user_data["email"],
                phone_number=user_data["phone_number"],
                date_registered=user_data["date_registered"]
            )

        self.stdout.write(self.style.SUCCESS('Successfully inserted EV user data'))
