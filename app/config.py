import os
from dotenv import load_dotenv
import pytz

load_dotenv()  # Load environment variables from .env file

# Twilio Configuration
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#API Key of calendar
GCALENDER_API_KEY = os.getenv("GCALENDER_API_KEY")

# Hindu Festival API
year = 2025
HINDU_CALENDAR_API = f"https://www.googleapis.com/calendar/v3/calendars/en.indian%23holiday@group.v.calendar.google.com"

# Time Zone
IST = pytz.timezone("Asia/Kolkata")
