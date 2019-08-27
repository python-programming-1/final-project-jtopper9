import requests
import pprint
import arrow


"""surf_favorites = [
{'name':"Breakwater", 'lat':33.984760, 'long'= -118.476433},
{'name':"El Porto", 'lat':33.901905, 'long'= -118.423384},
{'name':"Sunset", 'lat':34.036350, 'long'= -118.553784},
{'name':"Staircases", 'lat':34.046291, 'long'= -118.951108}
]

date_time_now = arrow.now('US/Pacific')
date_time_start = date_time_now.shift(hours=-1)
date_time_end = date_time_now.shift(hours=+1)
print(date_time_now)
print(date_time_start)
print(date_time_end)


response = requests.get(
  'https://api.stormglass.io/v1/weather/point',
  params={
    'lat': 33.984760,
    'lng': -118.476433,
    'start': date_time_start.to('UTC').timestamp,  # Convert to UTC timestamp
    'end': date_time_end.to('UTC').timestamp,  # Convert to UTC timestamp
    'source':"noaa"
  },
  headers={
    'Authorization': '9ddc9d2c-c6a0-11e9-ba13-0242ac130004-9ddca024-c6a0-11e9-ba13-0242ac130004'
  }
)

pprint.pprint(response.json())"""


api_results = {'hours': [{'airTemperature': [{'source': 'noaa', 'value': 27.07}],
            'cloudCover': [{'source': 'noaa', 'value': 0.0}],
            'currentDirection': [],
            'currentSpeed': [],
            'gust': [{'source': 'noaa', 'value': 1.35}],
            'humidity': [{'source': 'noaa', 'value': 46.9}],
            'precipitation': [{'source': 'noaa', 'value': 0.0}],
            'pressure': [{'source': 'noaa', 'value': 1014.82}],
            'seaLevel': [],
            'swellDirection': [{'source': 'noaa', 'value': 262.06}],
            'swellHeight': [{'source': 'noaa', 'value': 0.37}],
            'swellPeriod': [{'source': 'noaa', 'value': 12.48}],
            'time': '2019-08-25T17:00:00+00:00',
            'visibility': [{'source': 'noaa', 'value': 24.13}],
            'waterTemperature': [{'source': 'noaa', 'value': 32.99}],
            'waveDirection': [{'source': 'noaa', 'value': 173.17}],
            'waveHeight': [{'source': 'noaa', 'value': 0.98}],
            'wavePeriod': [{'source': 'noaa', 'value': 12.6}],
            'windDirection': [{'source': 'noaa', 'value': 230.67}],
            'windSpeed': [{'source': 'noaa', 'value': 1.75}],
            'windWaveDirection': [{'source': 'noaa', 'value': 186.85}],
            'windWaveHeight': [{'source': 'noaa', 'value': 0.36}],
            'windWavePeriod': [{'source': 'noaa', 'value': 11.58}]},
           {'airTemperature': [{'source': 'noaa', 'value': 28.8}],
            'cloudCover': [{'source': 'noaa', 'value': 0.0}],
            'currentDirection': [],
            'currentSpeed': [],
            'gust': [{'source': 'noaa', 'value': 1.4}],
            'humidity': [{'source': 'noaa', 'value': 39.9}],
            'precipitation': [{'source': 'noaa', 'value': 0.0}],
            'pressure': [{'source': 'noaa', 'value': 1014.65}],
            'seaLevel': [],
            'swellDirection': [{'source': 'noaa', 'value': 263.08}],
            'swellHeight': [{'source': 'noaa', 'value': 0.37}],
            'swellPeriod': [{'source': 'noaa', 'value': 12.96}],
            'time': '2019-08-25T18:00:00+00:00',
            'visibility': [{'source': 'noaa', 'value': 24.14}],
            'waterTemperature': [{'source': 'noaa', 'value': 36.51}],
            'waveDirection': [{'source': 'noaa', 'value': 173.56}],
            'waveHeight': [{'source': 'noaa', 'value': 0.98}],
            'wavePeriod': [{'source': 'noaa', 'value': 12.53}],
            'windDirection': [{'source': 'noaa', 'value': 236.9}],
            'windSpeed': [{'source': 'noaa', 'value': 1.9}],
            'windWaveDirection': [{'source': 'noaa', 'value': 186.5}],
            'windWaveHeight': [{'source': 'noaa', 'value': 0.35}],
            'windWavePeriod': [{'source': 'noaa', 'value': 11.54}]},
           {'airTemperature': [{'source': 'noaa', 'value': 30.55}],
            'cloudCover': [{'source': 'noaa', 'value': 16.67}],
            'currentDirection': [],
            'currentSpeed': [],
            'gust': [{'source': 'noaa', 'value': 2.07}],
            'humidity': [{'source': 'noaa', 'value': 34.83}],
            'precipitation': [{'source': 'noaa', 'value': 0.0}],
            'pressure': [{'source': 'noaa', 'value': 1014.18}],
            'seaLevel': [],
            'swellDirection': [{'source': 'noaa', 'value': 262.76}],
            'swellHeight': [{'source': 'noaa', 'value': 0.38}],
            'swellPeriod': [{'source': 'noaa', 'value': 12.96}],
            'time': '2019-08-25T19:00:00+00:00',
            'visibility': [{'source': 'noaa', 'value': 24.14}],
            'waterTemperature': [{'source': 'noaa', 'value': 38.41}],
            'waveDirection': [{'source': 'noaa', 'value': 173.68}],
            'waveHeight': [{'source': 'noaa', 'value': 0.98}],
            'wavePeriod': [{'source': 'noaa', 'value': 12.43}],
            'windDirection': [{'source': 'noaa', 'value': 237.57}],
            'windSpeed': [{'source': 'noaa', 'value': 2.59}],
            'windWaveDirection': [{'source': 'noaa', 'value': 186.89}],
            'windWaveHeight': [{'source': 'noaa', 'value': 0.33}],
            'windWavePeriod': [{'source': 'noaa', 'value': 11.45}]}],
 'meta': {'cost': 1,
          'dailyQuota': 50,
          'end': '2019-08-25 19:50',
          'lat': 33.98476,
          'lng': -118.476433,
          'params': ['waterTemperature',
                     'wavePeriod',
                     'waveDirection',
                     'waveDirection',
                     'waveHeight',
                     'windWaveDirection',
                     'windWaveHeight',
                     'windWavePeriod',
                     'swellPeriod',
                     'swellDirection',
                     'swellHeight',
                     'windSpeed',
                     'windDirection',
                     'airTemperature',
                     'precipitation',
                     'gust',
                     'cloudCover',
                     'humidity',
                     'pressure',
                     'visibility',
                     'seaLevel',
                     'currentSpeed',
                     'currentDirection'],
          'requestCount': 1,
          'source': 'noaa',
          'start': '2019-08-25 17:00'}}


hours_object = api_results['hours']

time_dict = {}
hourly_dict = {}
for hour in hours_object:
    for k, v in hour.items():
        empty = []
        if v == empty:
            pass
        elif isinstance(v, list):
            hourly_dict[k] = v[0]['value']
        else:
            hourly_dict[k] = v
            time_dict[str(hour.get('time', 0))] = hourly_dict

print(time_dict)

"""
new_dict = {}
for k, v in hours_object.items():
  empty = []
  if v == empty:
    pass
  elif isinstance(v, list):
    new_dict[k] = v[0]['value']
  else:
    new_dict[k] = v"""
