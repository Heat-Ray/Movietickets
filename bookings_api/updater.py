from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bookings_api.expiry_checker import check_expiry

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_expiry, 'interval', seconds=30)
    scheduler.start()
