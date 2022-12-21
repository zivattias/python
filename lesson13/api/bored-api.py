import requests
import json

BORED_URL = 'https://www.boredapi.com/api/activity'
response = requests.get(BORED_URL)

print('Bored API:')
print(response)
print(type(response))

print(response.status_code)
# print(response.text['activity']) <- won't work, since text isn't a dict class yet
response_json = response.json()     # transform response to a JSON
print(response_json)
print(response_json['activity'])    # get field 'activity' within the response

# Convert a JSON-representing string to a Python dictionary:
res = json.loads(response.text)
print(type(res))

print('\nGoogle:')
response = requests.get('https://www.google.com')
print(response.text)

print('\nEndpoint not found (/api/act):')
response = requests.get("https://www.boredapi.com/api/act")
print(response.status_code)
print(response.text)

print('\nBad URL:')
try:
    response = requests.get("https://bad_url")
except Exception as e:
    print(e)