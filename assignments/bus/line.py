import random
from datetime import datetime

from assignments.bus.ride import Ride


class Line:
    def __init__(self, line_num: int, origin: str, destination: str, stops: list[str]):
        self.line_num = line_num
        self.origin = origin
        self.destination = destination
        self.stops = stops
        # Each line instance has a scheduled rides map, {ride_id: Ride}
        self.rides: dict[int, Ride] = {}

    def __str__(self):
        return f"Line #{self.line_num}:\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.destination}\n" \
               f"Stops: {self.stops}\n" \
               f"Scheduled Rides:\n" \
               f"{self.rides}\n"

    def __repr__(self):
        rides = [key for key in self.rides]
        return f"<Line #{self.line_num}, Rides: {rides}>"

    def add_ride_to_line(self, departure_time: datetime.time, arrival_time: datetime.time, driver: str):
        ride_id = random.randint(1000, 9999)
        while ride_id in self.rides:
            ride_id = random.randint(1000, 9999)
        departure_object = datetime.strptime(departure_time, "%H:%M").time()
        self.rides[ride_id] = Ride(ride_id, departure_object, arrival_time, driver)
        return ride_id
