from django.db import models
from bookings_api.models import Booking
from datetime import datetime


def check_expiry():
    tickets = Booking.objects.all()
    for i in tickets:
        date_array = list(map(int, str(i.date).split('-')))
        time_array = list(map(int, str(i.time).split(':')))
        db_date_time = datetime(date_array[0], date_array[1], date_array[2], time_array[0], time_array[1], time_array[2])
        cur_date_time = datetime.now()
        diff = cur_date_time - db_date_time
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        if hours >= 8:
            i.status = 0
            i.save()
