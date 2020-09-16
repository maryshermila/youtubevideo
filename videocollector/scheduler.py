from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from videocollector import collectvideos

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(collectvideos.get_data, 'interval', minutes=1)
    scheduler.start()