from django.apps import AppConfig


class BookingsApiConfig(AppConfig):
    name = 'bookings_api'

    def ready(self):
        from bookings_api import time_scheduler
        time_scheduler.start()
