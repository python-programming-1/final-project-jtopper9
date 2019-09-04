import requests
import pprint
import arrow
import base64
import json
import pandas as pd
import config
import mimetypes
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


surf_favorites = [
{'name': "Breakwater", 'lat': 33.984760, 'long': -118.476433},
{'name': "El Porto", 'lat': 33.901905, 'long': -118.423384},
{'name': "Sunset", 'lat': 34.036350, 'long': -118.553784},
{'name': "Staircases", 'lat': 34.046291, 'long': -118.951108}
]

date_time_now = arrow.now('US/Pacific')
date_time_start = date_time_now.shift(hours=-1)
date_time_end = date_time_now.shift(hours=+1)

favorites_results = {}
for favorite in surf_favorites:
    # Call Stormglass API to request conditions for each surf spot
    response = requests.get(
    'https://api.stormglass.io/v1/weather/point',
        params={
        'lat': str(favorite.get('lat', 0)),
        'lng': str(favorite.get('long', 0)),
        'params': ','.join(['airTemperature', 'currentDirection', 'precipitation', 'seaLevel', 'swellDirection',
                            'swellHeight', 'swellPeriod', 'waterTemperature', 'waveHeight', 'wavePeriod',
                            'windDirection', 'windSpeed']),
        'start': date_time_start.to('UTC').timestamp,  # Convert to UTC timestamp
        'end': date_time_end.to('UTC').timestamp,  # Convert to UTC timestamp
        'source':"noaa"
        },
        headers={
        'Authorization': '9ddc9d2c-c6a0-11e9-ba13-0242ac130004-9ddca024-c6a0-11e9-ba13-0242ac130004'
        }
    )
    
    hours_object = response.json()

    # create a nested dictionary with the surf spot name as key
    favorites_results[str(favorite.get('name', 0))] = {}
    for hour in hours_object['hours']:
        # create a nested dictionary within the surf spot name, with the hour as key
        favorites_results[str(favorite.get('name', 0))][str(hour.get('time', 0))] = {}
        for k, v in hour.items():
            empty = []
            if v == empty:
                pass
            elif isinstance(v, list):
                value_1 = v[0]['value']
            else:
                value_1 = v
            favorites_results[str(favorite.get('name', 0))][str(hour.get('time', 0))][k] = value_1



# Set scope for GMAIL API
SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRETS_FILE = "client_secret.json"


# Google Oauth function
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build('gmail', 'v1', credentials=credentials)


# Google create email function
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


# Google send email function
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None



html_table = {}
for favorite, hour in favorites_results.items():
    df = pd.DataFrame(data=hour)
    df = df.fillna(' ').T
    html_table[favorite] = df.to_html()

dictlist = []


def printItems(dictObj, indent):
    for k,v in dictObj.items():
        print(' '*indent, '<h1>', k, '</h1>', v, '</br>')
        list_item = '<h1>' + k + '</h1>' + v + '</br>'
        dictlist.append(list_item)


printItems(html_table,0)

email_html = ""
for x in dictlist:
    email_html += x


sender_email = 'jeremy.topper9@gmail.com'
to_email = 'jtopper@connexity.com, jeremy.topper9@gmail.com'
subject_line = 'Daily Surf Report ' + arrow.now('US/Pacific').format('MM-DD-YYYY')
message_text_sample = email_html

service = get_authenticated_service()

raw_msg = create_message(sender_email, to_email, subject_line, message_text_sample)

send_message(service, sender_email, raw_msg)

