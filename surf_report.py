import requests
import pprint
import arrow
import base64
from email.mime.text import MIMEText
import mimetypes
# import os
# import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import pandas as pd
from flask_table import Table, Col


"""surf_favorites = [
{'name': "Breakwater", 'lat': 33.984760, 'long': -118.476433}
# {'name': "El Porto", 'lat': 33.901905, 'long': -118.423384},
# {'name': "Sunset", 'lat': 34.036350, 'long': -118.553784},
# {'name': "Staircases", 'lat': 34.046291, 'long': -118.951108}
]

date_time_now = arrow.now('US/Pacific')
date_time_start = date_time_now.shift(hours=-1)
date_time_end = date_time_now.shift(hours=+1)


time_dict = {}
favorites_results = {}

for favorite in surf_favorites:
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
    # print(hours_object)

    favorites_results[str(favorite.get('name', 0))] = {}
    for hour in hours_object['hours']:
        time_dict[str(hour.get('time', 0))] = {}
        for k, v in hour.items():
            empty = []
            if v == empty:
                pass
            elif isinstance(v, list):
                value_1 = v[0]['value']
            else:
                value_1 = v
            time_dict[str(hour.get('time', 0))][k] = value_1
        favorites_results[str(favorite.get('name', 0))] = time_dict

pprint.pprint(time_dict)
pprint.pprint(favorites_results)"""


SCOPES = 'https://www.googleapis.com/auth/gmail.compose'  # Allows sending only, not reading
CLIENT_SECRETS_FILE = "client_secret.json"


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build('gmail', 'v1', credentials=credentials)


def create_message(sender, to, subject, message_text):
    """Create a message for an email.3

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """

    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """

    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None


sample_response = {'2019-08-31T18:00:00+00:00': {'airTemperature': 29.44,
                               'currentDirection': 29.44,
                               'precipitation': 0.0,
                               'seaLevel': 0.0,
                               'swellDirection': 206.06,
                               'swellHeight': 0.37,
                               'swellPeriod': 14.98,
                               'time': '2019-08-31T18:00:00+00:00',
                               'waterTemperature': 36.79,
                               'waveHeight': 0.87,
                               'wavePeriod': 16.23,
                               'windDirection': 229.58,
                               'windSpeed': 2.4}}


"""sample_response1 = """\
""""<html>
<head></head>
<body>
<p>Contracts that need signed by jeremy<br>
<br>
<li>test email<br>
</body>
</html>
"""

"""niceText = pprint.pformat(sample_response)
htmlLines = []
for textLine in pprint.pformat(sample_response).splitlines():
    htmlLines.append('<br/>%s' % textLine)  # or something even nicer
htmlText = '\n'.join(htmlLines)

sample_response_json = json.dumps(sample_response).decode('utf-8')
sample_response_html = json.dumps(sample_response1).encode('utf-8')
sample_response_string = str(sample_response).encode('utf-8')"""

"""a = sample_response
df = pd.DataFrame(data=a)
df = df.fillna(' ').T
email_html = df.to_html()"""

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')


# Populate the table
table = ItemTable(sample_response)


sender_email = 'jeremy.topper9@gmail.com'
to_email = 'jtopper@connexity.com, jeremy.topper9@gmail.com'
subject_line = 'Daily Surf Report ' + arrow.now('US/Pacific').format('MM-DD-YYYY')
message_text_sample = table

service = get_authenticated_service()

raw_msg = create_message(sender_email, to_email, subject_line, message_text_sample)

send_message(service, sender_email, raw_msg)
