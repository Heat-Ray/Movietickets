from django.db import models

class Booking(models.Model):
    user_name = models.CharField(max_length = 40)
    phone_number = models.CharField(max_length = 13)
    timing = models.DateTimeField()
