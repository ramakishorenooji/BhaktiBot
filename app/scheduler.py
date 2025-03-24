from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.festival_service import get_hindu_festivals
from app.services.ai_service import generate_wish
from app.services.whatsapp_service import send_whatsapp_message
from app.config import IST
import time


contacts = {
    "+919743703515": "Ram"
}

def schedule_wishes():
    """Check today's festivals and send WhatsApp messages at 7 AM"""
    today = datetime.now(IST).strftime("%Y-%m-%d")
    festivals = get_hindu_festivals(datetime.now().year)

    for festival in festivals:
        if festival['start_date'] == today:
            for number, name in contacts.items():
                message = generate_wish(name, festival['summary'])
                send_whatsapp_message(number, message)
                time.sleep(1)

# Schedule the job
scheduler = BackgroundScheduler()
scheduler.add_job(schedule_wishes, 'cron', hour=8, minute=1, timezone=IST)
scheduler.start()
