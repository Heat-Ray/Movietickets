from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bookings_api.expiry_checker import check_expiry
from bookings_api.expired_ticket_remover import remove_expired_tickets

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_expiry, 'interval', seconds=30)
    scheduler.add_job(remove_expired_tickets, 'interval', seconds=110)
    scheduler.start()
