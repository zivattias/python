import os
import pickle

from assignments.bus.menu import Menu
from assignments.bus.bus_company import BusCompany
from assignments.bus.exceptions.exceptions import *

if __name__ == '__main__':
    if not os.path.exists('./bus_company.pickle'):
        bus_company = BusCompany()
        print('Found no existing companies, created empty one...')
    else:
        with open('./bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)
        print('Loaded existing company...')

    try:
        Menu(bus_company).run()

    # except (LineExists, LineMissing, InvalidStopsString, InvalidLineAttribute, RideNotFound) as e - won't work
    # for some reason, need clarification as for why
    except Exception as e:
        print(e)
        with open('./bus_company.pickle', 'wb') as fh:
            pickle.dump(bus_company, fh)
            print('Saved company database!')
