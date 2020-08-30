from django.db import models
from bookings_api.models import Booking

def remove_expired_tickets():
    tickets = Booking.objects.all()
    for i in tickets:
        if i.status == 0:
            i.delete()
