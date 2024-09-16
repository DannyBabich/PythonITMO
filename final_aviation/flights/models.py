from django.db import models
from django.utils.timezone import now


class Aircraft(models.Model):
    icao24 = models.CharField(max_length=6, unique=True)
    callsign = models.CharField(max_length=8, null=True, blank=True)
    origin_country = models.CharField(max_length=64)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    velocity = models.FloatField(null=True, blank=True)
    heading = models.FloatField(null=True, blank=True)
    last_contact = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.callsign} ({self.icao24})'
