from assignments.bus.bus_company import BusCompany
from assignments.bus.exceptions.exceptions import *
import pickle


class Menu:
    MANAGER_OPTIONS = {'1': 'Add a line', '2': 'Delete a line', '3': 'Update a line', '4': 'Add a ride to a line',
                       '5': 'Save company database'}

    PASSENGER_OPTIONS = {'1': 'Line lookup', '2': 'Report delay', '3': 'Ride lookup', '4': 'Exit'}

    def __init__(self, bus_company):
        self.bus_company: BusCompany = bus_company

    def password_checker(self):
        x = 1
        print('ADMIN AUTH: Enter password.')
        while x <= 4:
            if x == 4:
                print(f'{x - 1} tries were used. Exiting...')
                with open('./bus_company.pickle', 'wb') as fh:
                    pickle.dump(self.bus_company, fh)
                    print('Saved company database!')
                    exit()
            password = input('>> ')
            if password != 'RideWithUs!':
                print(f'ADMIN AUTH: Wrong password! ({3 - x} tries left)')
                x += 1
                continue
            break

    def run(self):

        print('Welcome to Bus Manager 1.0, you can log-in as manager or choose to use'
              'the app as a passenger.\n'
              'LOG-IN: Who would you like to log-in as? (M - Manager, P - Passenger)')
        while True:
            role = input('>> ').upper()
            if role not in ['M', 'P']:
                print(f"Wrong input: {role}. Please choose M/Y.")
                continue
            break
        if role == 'M':
            self.password_checker()

            while True:
                print(self.MANAGER_OPTIONS)
                action = input('>> ')
                if action not in self.MANAGER_OPTIONS:
                    print(f"Wrong input {action}. Choose from: {self.MANAGER_OPTIONS}")
                    continue

                if action != '5':
                    line_num = int(input('Enter a line number: '))

                if action == '1':
                    origin = input('Enter origin station: ')
                    destination = input('Enter destination station: ')
                    stops = input('Enter stops, separated with a comma: ')
                    self.bus_company._add_line(line_num, origin, destination, stops)

                elif action == '2':
                    self.bus_company._del_line(line_num)

                elif action == '3':
                    print(self.bus_company._get_line(line_num))
                    criteria = input('Enter a criteria to update (origin, destination, stops): ').lower()
                    new_data = input('Enter new data: ')
                    self.bus_company._update_line(line_num, criteria, new_data)
                    print(self.bus_company._get_line(line_num))

                elif action == '4':
                    departure_time = input('Enter departure time (HH:MM): ')
                    arrival_time = input('Enter arrival time (HH:MM): ')
                    driver = input("Enter driver's name: ")
                    self.bus_company._add_ride_to_line(line_num, departure_time, arrival_time, driver)

                elif action == '5':
                    with open('./bus_company.pickle', 'wb') as fh:
                        pickle.dump(self.bus_company, fh)
                        print('Saved company database!')
                        exit()

        if role == 'P':
            while True:
                print(self.PASSENGER_OPTIONS)
                action = input('>> ')
                if action not in self.PASSENGER_OPTIONS:
                    print(f"Wrong input {action}. Choose from: {self.PASSENGER_OPTIONS}")
                    continue

                if action == '1':
                    query = input('Line lookup. Enter a line number, origin, destination or stop name: ')
                    print(self.bus_company.p_get_line(query))

                if action == '2':
                    print('Report Delay: First find a line, then report a delay to one of its rides')
                    query = input('Enter a line number, origin, destination or stop name: ')
                    print(self.bus_company.p_get_line(query))
                    ride_id = int(input('Enter ride ID: '))
                    delay = int(input('Enter delay in minutes: '))
                    print(self.bus_company.p_report_delay(ride_id, delay))

                if action == '3':
                    ride_id = int(input('Enter a ride ID to lookup: '))
                    print(self.bus_company.get_ride(ride_id))

                if action == '4':
                    with open('./bus_company.pickle', 'wb') as fh:
                        pickle.dump(self.bus_company, fh)
                        print('Saved your actions!')
                        exit()
