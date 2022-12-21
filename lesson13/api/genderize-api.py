import requests

GENDERIZE_URL = "https://api.genderize.io/"
response = requests.get(GENDERIZE_URL, params={'name': 'valeria'})

print(response.status_code, response.text, sep='\n')
response_json = response.json()
print(response_json['name'], response_json['gender'], response_json['probability'], sep='\n')

#

SOME_URL = "https://api.genderize.io/blah"
response_2 = requests.get(SOME_URL)

print(f"Status code for {SOME_URL}: {response.status_code}")

if __name__ == '__main__':
    name = input('Enter your name: ')
    response = requests.get(GENDERIZE_URL, params={'name': name})
    if response.status_code == 200:
        name_dict = response.json()
        print(f"Your name is a {name_dict['gender']} name, with a probability of: %{name_dict['probability'] * 100}.")
    else:
        print(f"Error: {response.status_code}")
