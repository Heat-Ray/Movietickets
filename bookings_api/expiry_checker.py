from django.db import models
from bookings_api.models import Booking
from datetime import datetime


def check_expiry():
    tickets = Booking.objects.all()
    for i in tickets:
        print(i)
