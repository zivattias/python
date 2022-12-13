import os
import pickle
from assignments.bus.bus_company import BusCompany

if __name__ == '__main__':
    if not os.path.exists('./bus_company.pickle'):
        bus_company = BusCompany()
    else:
        with open('./bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    #
    # here comes your code that runs main menu
    # and interacts with the user and adds/ updates
    # data in your bus_company class

    # before exiting the program, persist the current state
    # of te system in the file, so next time it will be loaded
    with open('./bus_company.pickle', 'wb') as fh:
        pickle.dump(bus_company, fh)
