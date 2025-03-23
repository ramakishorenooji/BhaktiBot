from celery import Celery
from app.services.whatsapp_service import send_whatsapp_message

celery_app = Celery(
    "festival_wisher",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def send_festival_wish_task(phone_number: str, message: str):
    """Celery task to send WhatsApp messages"""
    send_whatsapp_message(phone_number, message)
