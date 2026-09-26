from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location_details = models.CharField(max_length=255)
    capacity = models.PositiveBigIntegerField()


    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    titled = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='SCHEDULED')

    def __str__(self):
      return self.title

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rsvp_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f" {self.user.username} - {self.event.title}"



