import time
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from app.config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(phone_number: str, message: str):
    """Send a WhatsApp message using Twilio"""
    try:
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=f"whatsapp:{phone_number}"
        )
    except TwilioRestException as e:
        if "rate limit" in str(e):
            time.sleep(1)  # Wait for 1 second before retrying
            send_whatsapp_message(phone_number, message)
        else:
            raise e