import requests
from exceptions import *


class SpotifyAPI:
    def __init__(self, username):
        self._username = username
        self._search_track_url = "https://api.spotify.com/v1/search"
        self._create_playlist_url = f"https://api.spotify.com/v1/users/{username}/playlists"
        self._add_tracks_to_playlist_url = None

        self._headers = {
            'Accept': 'application-json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer BQAf2wxPQ-_EutwE9M9gukE4QPvx3GyA4UymhkYykArvEy44UppKIyEwgmcCx0yDyuA6BWQokcIw_nuU855UsvdumkKMY-00xyeuGyc_scGOe3wNQ7TDXI3k8IrgYKc8Qe0Q6_jDB1bzdNoOAE8DzRAFbquKlZgh4-U0SMsRuF8oQtijb93GAs3ikkiUYtajugpOll0dGruQVwRhgyVRnKnq_cH4-45K8q3xGTGEkP28'
        }

        self._tracks: dict[str, str] = dict()
        self._playlist_uri = None

    def get_track(self, query):
        response = requests.get(self._search_track_url,
                                headers=self._headers,
                                params={'q': query, 'type': 'track', 'market': 'IL', 'limit': '1', 'offset': '0'})

        if response.status_code == 200 or response.status_code == 201:
            json_resp = response.json()

            # If track query is invalid:
            if len(json_resp['tracks']['items']) == 0:
                raise SpotifyInvalidTrack(query)

            # Tracks Dict: self.tracks[track_uri] = f"Musician - SongName"
            self._tracks[
                json_resp['tracks']['items'][0]['uri']] = \
                f"{json_resp['tracks']['items'][0]['artists'][0]['name']} - {json_resp['tracks']['items'][0]['name']}"

            return f"{json_resp['tracks']['items'][0]['artists'][0]['name']}" \
                   f" - {json_resp['tracks']['items'][0]['name']}"

        raise SpotifyServerError()

    def create_empty_playlist(self, playlist_name, playlist_desc):
        metadata = {
            'name': playlist_name,
            'description': playlist_desc,
            'public': True
        }

        response = requests.post(self._create_playlist_url, headers=self._headers, json=metadata)

        if response.status_code == 200 or response.status_code == 201:
            json_resp = response.json()
            self._playlist_uri = json_resp['uri']
            self._add_tracks_to_playlist_url = f"https://api.spotify.com/v1/playlists/{json_resp['id']}/tracks"
            return self._playlist_uri

        raise SpotifyServerError()

    def get_playlist_uri(self):
        return self._playlist_uri

    def count_tracks(self):
        return len(self._tracks)

    def get_tracks(self):
        return self._tracks

    def get_username(self):
        return self._username

    def add_tracks_to_playlist(self):
        all_tracks_string = ""
        for track_uri in self._tracks.keys():
            if not all_tracks_string:
                all_tracks_string += track_uri
            else:
                all_tracks_string += f",{track_uri}"

        response = requests.post(self._add_tracks_to_playlist_url,
                                 params={'uris': all_tracks_string},
                                 headers=self._headers)

        if response.status_code == 200 or response.status_code == 201:
            return True
        raise SpotifyServerError()


if __name__ == '__main__':
    try:
        spotify = SpotifyAPI('zivattias7')
        print(f"Welcome to {spotify.get_username()}'s playlist manager, powered by Spotify Web API")
        print("First, let's create an empty playlist!")

        while True:
            pl_name = input("Enter the playlist's title: ")
            if not pl_name:
                print('You must provide a title.')
                continue
            break
        while True:
            pl_desc = input("Let's give it some description: ")
            if not pl_desc:
                print('You must provide a description.')
                continue
            break

        spotify.create_empty_playlist(playlist_name=pl_name, playlist_desc=pl_desc)

        print(f"Your playlist has been created. This is its Spotify URI: {spotify.get_playlist_uri()}")
        print("Great! Let's add some tracks to our playlist!")

        while True:
            try:
                track = input("Track name ('$' to finish): ")
                if track == '$':
                    if spotify.count_tracks() < 1:
                        print("Let's add at least one track prior to finishing the process.")
                        continue
                    break
                print(spotify.get_track(track))
            except SpotifyInvalidTrack as e:
                print(e)

        spotify.add_tracks_to_playlist()
        print('Added tracks:')
        for i, value in enumerate(spotify.get_tracks().values()):
            print(f"{i + 1}. {value}")

    except SpotifyException as e:
        print(e)
