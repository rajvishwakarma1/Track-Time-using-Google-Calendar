import os
import datetime
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def authenticate_google_calendar():
    """Authenticate and return the Google Calendar service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def create_calendar_event(service, summary, description, start_time, end_time):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',  # Use 'Asia/Kolkata' for New Delhi
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',  # Use 'Asia/Kolkata' for New Delhi
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")

def format_duration(start_time, end_time):
    duration = end_time - start_time
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)} hours {int(minutes)} mins {int(seconds)} secs"

def main():
    service = authenticate_google_calendar()
    
    # Record the start time when the script is executed
    start_time = datetime.datetime.now()
    print("Session started at:", start_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Ask for session type
    session_type = input("Enter the type of session (e.g., Meeting, Study, etc.): ").strip()
    if not session_type:
        session_type = "Coding Session"

    # Ask for additional description
    session_additional_description = input("Enter additional description for the session (optional): ").strip()

    # Wait for the user to input "end" to end the session
    while True:
        user_input = input("Type 'end' to end the session: ")
        if user_input.lower() == 'end':
            break

    # Record the end time when the user ends the session
    end_time = datetime.datetime.now()
    print("Session ended at:", end_time.strftime("%Y-%m-%d %H:%M:%S"))

    # Calculate duration
    duration_str = format_duration(start_time, end_time)

    # Create description with session type, elapsed time, and additional description
    session_description = f"{session_type}: {duration_str}"
    if session_additional_description:
        session_description += f" ({session_additional_description})"

    # Create event in Google Calendar
    create_calendar_event(service, session_type, session_description, start_time.isoformat(), end_time.isoformat())

if __name__ == '__main__':
    main()
