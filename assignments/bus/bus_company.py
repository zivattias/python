from datetime import datetime, timedelta

from assignments.bus.line import Line
from assignments.bus.ride import Ride
from exceptions.exceptions import *


class BusCompany:

    def __init__(self):

        self.lines: dict[int: Line] = {}
        self.lines_by_origin: dict[str: Line] = {}
        self.lines_by_destination: dict[str: Line] = {}
        self.lines_by_stops: dict[str: Line] = {}

        self.rides: dict[int: Ride] = {}

    @staticmethod
    def stops_converter(stops: str) -> list:
        if stops.count(',') < 1:
            raise InvalidStopsString

        return [stop.strip() for stop in stops.split(',')]

    def _add_line(self, line_num: int, origin: str, destination: str, stops: str):
        if line_num in self.lines:
            raise LineExists(line_num)

        stops_list = self.stops_converter(stops)
        line = Line(line_num, origin, destination, stops=stops_list)

        self.lines[line_num] = line

        if origin not in self.lines_by_origin:
            self.lines_by_origin[origin] = []
        self.lines_by_origin[origin].append(line)

        if destination not in self.lines_by_destination:
            self.lines_by_destination[destination] = []
        self.lines_by_destination[destination].append(line)

        for stop in stops_list:
            if stop not in self.lines_by_stops:
                self.lines_by_stops[stop] = []
            self.lines_by_stops[stop].append(line)

        return True

    def _del_line(self, line_num: int):
        if line_num not in self.lines:
            raise LineMissing(line_num)

        self.lines.pop(line_num)

        return True

    def _get_line(self, line_num: int) -> Line:
        if line_num not in self.lines:
            raise LineMissing(line_num)

        return self.lines[line_num]

    def _update_line(self, line_num, criteria: str, new_data: str):
        line = self._get_line(line_num)

        if criteria not in dir(line):
            raise InvalidLineAttribute(criteria)

        if criteria == 'stops':
            setattr(line, criteria, self.stops_converter(new_data))
            return True

        setattr(line, criteria, new_data)

        return True

    def _get_line_rides(self, line_num: int):
        line = self._get_line(line_num)

        return line.rides.values()

    def _add_ride_to_line(self, line_num, departure_time: datetime.time, arrival_time: datetime.time, driver: str):
        line = self._get_line(line_num)
        ride_id = line.add_ride_to_line(departure_time, arrival_time, driver)
        self.rides[ride_id] = self.get_ride(ride_id)

        return True

    def p_get_line(self, query: str):
        # If search query is a digit (=line num):
        if query.isdigit():
            return self._get_line(int(query))
        # If search query is a string (=origin/destination/stop):
        ret_val = list()
        # Query can be equal to origin/destination/stop and vice versa, thus resulting in a DB-wide iteration:
        for db in [self.lines_by_origin, self.lines_by_destination, self.lines_by_stops]:
            if query in db.keys():
                ret_val.extend(db[query])
        return ret_val

    def get_ride(self, ride_id: int):
        for line in self.lines.values():
            for ride in line.rides.values():
                if ride_id == ride.ride_id:
                    return ride

    def p_report_delay(self, query: int | str, ride_id: int, delay: int):
        print(self.p_get_line(query))
        ride = self.get_ride(ride_id)
        ride.delays += timedelta(seconds=delay * 60)
        ride.arrival_time += ride.delays
        return ride

#TODO:
    #Add exceptions and/or returns to ALL functions
    #Get ride for passenger shouldn't display driver name
    #Build menu classes
    #Construct __main__


comp = BusCompany()

comp._add_line(1, 'hi', 'bye', 'a,b,c')
comp._add_line(2, 'b', 'bye', 'a,b,c')
comp._add_line(3, 'hi', 'bye', 'a,b,c')
comp._add_ride_to_line(3, '23:00', '23:30', 'Ziv')
comp._add_ride_to_line(3, '23:00', '23:30', 'Ziv')
comp._add_ride_to_line(2, '23:00', '23:30', 'David')
comp._add_ride_to_line(1, '23:05', '23:30', 'Michael')
print(comp.p_get_line("3"))
print(comp.p_get_line("2"))
print(comp.p_get_line("bye"))
# print(comp.p_report_delay('1', 999, 15))
