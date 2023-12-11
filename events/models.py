from django.db import models

class Event(models.Model):
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.TimeField()
    location_address = models.CharField(max_length=255)
    venue_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    details = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.venue_name} - {self.date} {self.time}'
