# B5.5
# my_cities = {
#    2008:{'Germany':['Berlin', 'Munich'],
#            'France' :['Paris','Leon','Bordeaux']},
#    2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
#             'Japan':['Nagoya','Toyokawa','Yatomi'],
#             'Mexico':['Tijuana','Ecatepec']},
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#             'France': ['Paris', 'Nice', 'Bordeaux'],
#             'Japan':['Tokyo','Toyokawa','Yatomi']}
# }
# Create a function that receives my_cities and returns all the cities I’ve visited without duplications.
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

def unique_cities(d: dict[int, dict[str: list]]) -> set:
    s = set()
    for year in d:
        for country in d[year]:
            for city in d[year][country]:
                s.add(city)
    return s

pprint.pprint(unique_cities(my_cities))
