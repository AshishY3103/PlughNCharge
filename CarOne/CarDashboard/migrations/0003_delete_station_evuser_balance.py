# Generated by Django 5.0.2 on 2024-03-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDashboard', '0002_station'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.AddField(
            model_name='evuser',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
