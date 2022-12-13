from apscheduler.schedulers.background import BackgroundScheduler
import time

from motivator import send_whatsapp_text,Client,quote

scheduler=BackgroundScheduler(timezone='Asia/Kolkata')
scheduler.start()

job=scheduler.add_job(send_whatsapp_text,'cron',[Client,quote],hour='12',minute='40')

print(job)

while True:
    time.sleep(1)