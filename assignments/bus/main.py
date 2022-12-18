import os
import pickle

from assignments.bus.menu import Menu
from assignments.bus.bus_company import BusCompany


if __name__ == '__main__':
    if not os.path.exists('./bus_company.pickle'):
        bus_company = BusCompany()
        print('Found no existing companies, created empty one...')
    else:
        with open('./bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)
        print('Loaded existing company...')

    menu = Menu(bus_company).run()
