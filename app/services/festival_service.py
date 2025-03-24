import requests
from app.config import HINDU_CALENDAR_API, GCALENDER_API_KEY


def get_hindu_festivals(year: int):
    """Fetch Hindu festival dates from the API"""
    response = requests.request(
        "GET",
        f"{HINDU_CALENDAR_API}/events?timeMin={year}-01-01T00:00:00Z&timeMax={year}-12-31T23:59:59Z&key={GCALENDER_API_KEY}"
    )
    events = response.json().get("items", [])
    # Sort events by start date
    events.sort(key=lambda x: x.get("start", {}).get("date", ""))

    # Create a dictionary with required fields
    sorted_events = [
        {
            "summary": event.get("summary"),
            "start_date": event.get("start", {}).get("date"),
            "end_date": event.get("end", {}).get("date"),
            "id": event.get("id"),
            "status": event.get("status"),
        }
        for event in events
    ]
    # response = requests.get(f"{HINDU_CALENDAR_API}?year={year}&country=IN")
    print("This is the sorted events", sorted_events)
    
    return sorted_events if response.status_code == 200 else []
