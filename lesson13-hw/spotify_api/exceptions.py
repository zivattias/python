class SpotifyException(Exception):
    def __init__(self, s):
        super().__init__(s)

class SpotifyServerError(SpotifyException):
    def __init__(self):
        super().__init__("Response Code != 200, server error")


class SpotifyInvalidTrack(SpotifyException):
    def __init__(self, track):
        super().__init__(f"Track '{track}' wasn't found in Spotify servers")