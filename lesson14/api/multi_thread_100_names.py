import time
from datetime import datetime

import requests
import pytz
from pytz import timezone
import concurrent
from concurrent.futures import ThreadPoolExecutor, wait


class BadResponse(Exception):
    def __init__(self, val):
        super().__init__(f'Bad response received from API path, given value: {val}')


class BadNameGiven(BadResponse):
    def __init__(self, val):
        super().__init__(val=val)


class NationalizeAPI:
    NATIONALIZE_URL = "https://api.nationalize.io/"
    COUNTRY_ALPHA_CODE_URL = "https://restcountries.com/v3.1/alpha/"

    def __init__(self, names: list[str]):
        self._names = names

    @staticmethod
    def _get_response(url, name: str = None, code: str = None):
        if name is not None:
            return requests.get(url, params={'name': name})
        elif code is not None:
            return requests.get(url + code)
        else:
            raise BadResponse('unspecified name/country-code')

    def _get_json_dict(self, name: str):
        response = self._get_response(url=self.NATIONALIZE_URL, name=name)
        if response.status_code == 200:
            nationalize_dict = response.json()
            if len(nationalize_dict['country']) == 0:
                raise BadNameGiven(name)
            else:
                return nationalize_dict
        else:
            raise BadResponse(response.status_code)

    def get_most_probable_country(self, name: str):
        countries = []

        for i, c in enumerate(self._get_json_dict(name)['country']):
            if c['country_id'] == 'SQ':
                countries.append(['LC'])
            else:
                countries.append([c['country_id']])
            countries[i].append(c['probability'])

        return sorted(countries, key=lambda x: x[1], reverse=True)[0][0]

    def get_country(self, name: str):
        first_place_country = self.get_most_probable_country(name)
        response = self._get_response(url=self.COUNTRY_ALPHA_CODE_URL, code=first_place_country)
        if response.status_code == 200:
            country_data_dict = response.json()
            return (country_data_dict[0]['name']['official'],
                    country_data_dict[0]['continents'],
                    country_data_dict[0]['languages'].values(),
                    country_data_dict[0]['timezones'])

    def get_names(self):
        return self._names


if __name__ == '__main__':
    try:
        start = time.time()
        nationalize = NationalizeAPI(
            ["Aaron", "Abdul", "Abe", "Abel", "Abraham", "Abram", "Adalberto", "Adam", "Adan", "Adolfo", "Adolph",
             "Adrian", "Agustin", "Ahmad", "Ahmed", "Al", "Alan", "Albert", "Alberto", "Alden", "Aldo", "Alec",
             "Alejandro", "Alex", "Alexander", "Alexis", "Alfonso", "Alfonzo", "Alfred", "Alfredo", "Ali", "Allan",
             "Allen", "Alonso", "Alonzo", "Alphonse", "Alphonso", "Alton", "Alva", "Alvaro", "Alvin", "Amado",
             "Ambrose", "Amos", "Anderson", "Andre", "Andrea", "Andreas", "Andres", "Andrew", "Andy", "Angel", "Angelo",
             "Anibal", "Anthony", "Ziv", "Antoine", "Anton", "Antone", "Antonia", "Antonio", "Antony", "Antwan",
             "Archie", "Arden", "Ariel", "Arlen", "Arlie", "Armand", "Armando", "Arnold", "Arnoldo", "Arnulfo", "Aron",
             "Arron", "Art", "Arthur", "Arturo", "Asa", "Ashley", "Aubrey", "August", "Augustine", "Augustus",
             "Aurelio", "Austin", "Avery"])


        def flow(name: str):
            country = nationalize.get_country(name)[0]
            continent = nationalize.get_country(name)[1]
            languages = nationalize.get_country(name)[2]
            timezones = nationalize.get_country(name)[3]
            return name, country, continent, languages, timezones


        def get_time(name: str):
            country_timezones = pytz.country_timezones[nationalize.get_most_probable_country(name)]  # [Asia/Jerusalem]
            for country_time in country_timezones:
                curr_time = pytz.utc.localize(datetime.utcnow(), is_dst=None).astimezone(timezone(country_time))
                print(f"> Timezone: {country_time}, Time: {curr_time.strftime('%H:%M')}")
            print("\n")


        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = []
            for name in nationalize.get_names():
                future = executor.submit(flow, name)
                futures.append(future)

        done, not_done = wait(futures)

        for (name, future) in zip(nationalize.get_names(), done):
            print(f"Name: {future.result()[0]}",
                  f"Country: {future.result()[1]}",
                  f"Continent: {future.result()[2]}",
                  f"Languages: {future.result()[3]}",
                  f"All Timezones: {future.result()[4]}", sep="\n")
            get_time(name)

        elapsed = time.time() - start
        print(f"Time elapsed: {elapsed}")

        with open('time_log.txt', 'a') as f:
            f.write(f'Multi thread elapsed time (100 names): {elapsed}\n')

    except BadResponse as e:
        print(e)
