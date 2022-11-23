# B5.6
# Input dictionary for example
# my_cities = {
#    2008: {'Germany': ['Berlin', 'Munich'],
#           'France': ['Paris', 'Leon', 'Bordeaux']},
#
#    2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
#           'Japan': ['Nagoya', 'Toyokawa', 'Yatomi'],
#           'Mexico': ['Tijuana', 'Ecatepec']},
#
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#           'France': ['Paris', 'Nice', 'Bordeaux'],
#           'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}
# }
# Create a function that receives my_cities and returns dictionary arranged as follows:
# Keys = cities
# Values = all dates when I was visiting the cities
# Example of output:
# my_cities_out = {'Berlin':[2008, 2010],....}

import pprint

my_cities = {
   2008: {'Germany': ['Berlin', 'Munich'],
          'France': ['Paris', 'Leon', 'Bordeaux']},

   2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
          'Japan': ['Nagoya', 'Toyokawa', 'Yatomi'],
          'Mexico': ['Tijuana', 'Ecatepec']},

   2010: {'Germany': ['Berlin', 'Dusseldorf'],
          'France': ['Paris', 'Nice', 'Bordeaux'],
          'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}
}

def new_dict(d: dict[int: dict[str, list]]) -> dict[str: list[int]]:
    d1 = dict()
    # Example of output:
    # my_cities_out = {'Berlin':[2008, 2010],....}
    for year in d:
        for country in d[year]:
            for city in d[year][country]:
                d1[city] = list()

    for year in d:
        for country in d[year]:
            for city in d[year][country]:
                d1[city].append(year)
    return d1

pprint.pprint(new_dict(my_cities))