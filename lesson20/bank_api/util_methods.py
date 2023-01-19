from configparser import ConfigParser

__all__ = [
    'params',
    'endpoint',
    'dictify'
]

_API_URL = 'http://127.0.0.1'
_ENDPOINT = '/api'


def _get_config(filename='config.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db_config = dict()
    if parser.has_section(section=section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in {1} file".format(section, filename))
    return db_config


def params(filename='config.ini', section='postgresql'):
    return _get_config(filename, section)


def endpoint():
    return _API_URL + _ENDPOINT


def dictify(d: dict) -> dict:
    return {
        'data': d
    }
