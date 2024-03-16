# Generated by Django 5.0.2 on 2024-03-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('location', models.FloatField(blank=0.0, null=True)),
            ],
        ),
    ]
