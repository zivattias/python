# from assignments.bus.bus_company import BusCompany
#
#
# class Menu:
#     MANAGER_MENU = '''
#     Choose an option by its designated number:
#     1) Add Line
#     2) Delete Line
#     3) Update Line (Origin, Destination or Stops)
#     4) Add Ride to Line
#     '''
#
#     MANAGER_OPTIONS = [1, 2, 3, 4]
#
#     PASSENGER_MENU = '''
#     Choose an option by its designated number:
#     1) Search for a Line
#     2) Report Delay
#     '''
#
#     PASSENGER_OPTIONS = [1, 2]
#
#     @staticmethod
#     def password_checker():
#         x = 1
#         print('ADMIN AUTH: Enter password.')
#         while x < 4:
#             if x == 3:
#                 print(f'{x} tries were used. Exiting...')
#                 exit()
#             password = input('>> ')
#             if password != 'RideWithUs!':
#                 print(f'ADMIN AUTH: Wrong password! ({3 - x} tries left)')
#                 x += 1
#             break
#
#     def run(self):
#
#         print('Welcome to Bus Manager 1.0, you can log-in as manager or choose to use'
#               'the app as a passenger.\n'
#               'LOG-IN: Who would you like to log-in as? (M - Manager, P - Passenger)')
#         while True:
#             role = input('>> ').upper()
#             if role not in ['M', 'Y']:
#                 print(f"Wrong input: {role}. Please choose M/Y.")
#             break
#         if role == 'M':
#             self.password_checker()
#             print(self.MANAGER_MENU)
#             while True:
#                 action = input('>> ')
#                 if not action.isdigit() or int(action) not in self.MANAGER_OPTIONS:
#                     print(f"Wrong input {action}. Choose from: {self.MANAGER_OPTIONS}")
#                 match int(action):
#                     case 1:
#                         line_num = input('Enter a line number: ')
#                         origin = input('Enter origin station: ')
#                         destination = input('Enter destination station: ')
#                         stops = input('Enter stops, separated with a comma: ')
#                         BusCompany._add_line(line_num, origin, destination, stops)
