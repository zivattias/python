from configparser import ConfigParser

__all__ = [
    'get_config'
]

def get_config(filename='config.ini', section='postgresql'):
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
