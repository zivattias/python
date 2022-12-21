from datetime import datetime

import requests
import pytz
from pytz import timezone


class BadResponse(Exception):
    def __init__(self, val):
        super().__init__(f'Bad response received from API path, given value: {val}')


class BadNameGiven(BadResponse):
    def __init__(self, val):
        super().__init__(val=val)


class NationalizeAPI:
    NATIONALIZE_URL = "https://api.nationalize.io/"
    COUNTRY_ALPHA_CODE_URL = "https://restcountries.com/v3.1/alpha/"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def _get_response(url, name: str = None, code: str = None):
        if name is not None:
            return requests.get(url, params={'name': name})
        elif code is not None:
            return requests.get(url + code)
        else:
            raise BadResponse('unspecified name/country-code')

    def _get_json_dict(self):
        response = self._get_response(url=self.NATIONALIZE_URL, name=self.name)
        if response.status_code == 200:
            nationalize_dict = response.json()
            if len(nationalize_dict['country']) == 0:
                raise BadNameGiven(self.name)
            else:
                return nationalize_dict
        else:
            raise BadResponse(response.status_code)

    def get_most_probable_country(self):
        countries = []

        for i, c in enumerate(self._get_json_dict()['country']):
            countries.append([c['country_id']])
            countries[i].append(c['probability'])

        return sorted(countries, key=lambda x: x[1], reverse=True)[0][0]

    def get_country(self):
        first_place_country = self.get_most_probable_country()
        response = self._get_response(url=self.COUNTRY_ALPHA_CODE_URL, code=first_place_country)
        if response.status_code == 200:
            country_data_dict = response.json()
            return (country_data_dict[0]['name']['official'],
                    country_data_dict[0]['continents'],
                    country_data_dict[0]['languages'].values(),
                    country_data_dict[0]['timezones'])


if __name__ == '__main__':
    try:
        nationalize = NationalizeAPI('Boris')
        country = nationalize.get_country()[0]
        continent = nationalize.get_country()[1]
        languages = nationalize.get_country()[2]
        timezones = nationalize.get_country()[3]
        # curr_time = [pytz.utc.localize(timezone, is_dst=None).astimezone() for timezone in timezones]
        print(f"Country: {country}",
              f"Continent: {continent}",
              f"Languages: {languages}",
              f"All Timezones: {timezones}", sep="\n")

        country_timezone = pytz.country_timezones[nationalize.get_most_probable_country()]  # [Asia/Jerusalem]
        for country_time in country_timezone:
            curr_time = pytz.utc.localize(datetime.utcnow(), is_dst=None).astimezone(timezone(country_time))
            print(f"> Timezone: {country_time}, Time: {curr_time.strftime('%H:%M')}")

    except BadResponse as e:
        print(e)
