from django.contrib import admin
from .models import Venue, Event, RSVP

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'location_details', 'capacity']
    search_fields = ['name']

@admin.register(Event)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_time', 'venue', 'organizer', 'status']
    list_display = ['status', 'date_time']
    search_fields = ['title', 'description']

@admin.register(RSVP)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'rsvp_date']
