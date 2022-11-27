# Class creation:

class Car:
    def __init__(self, manufacturer: str, model: str,
                 color: str, fuel_consumption: float,
                 fuel_tank_capacity: int,
                 year: int = None):
        # print(f'Inside of __init__ of {manufacturer}')
        self.manufacturer: str = manufacturer
        self.model: str = model
        self.color: str = color
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity
        self.km: int = 0
        self.fuel: float = 0
        self.year: int = year
        self.fixes: dict = {}

    def __str__(self):
        print('Inside of __str__')
        return f"{self.manufacturer} | Model: {self.model}  | Year: {self.year}"

    def display_dashboard(self):
        print(f"{self.manufacturer} {self.model}'s fuel data:\n"
              f"Fuel left: {self.fuel} L\n"
              f"KM: {self.km}\n")

    def fill_tank(self, amount: float) -> bool:
        print(f'Filled tank with {amount} L.')
        if amount <= 0:
            print('Non-positive amount is not allowed.')
            return False
        if amount + self.fuel > self.fuel_tank_capacity:
            print('Cannot fill more than the tank capacity.\n'
                  f'Current capacity is: {self.fuel} l')
            return False

        self.fuel += amount
        return True

    def drive(self, kms_drove):
        used_fuel = kms_drove / 100 * self.fuel_consumption
        if self.fuel == 0:
            print("Can't drive without fuel, refill tank.")
        elif kms_drove < 0:
            print("KMs drove should be positive.")
        if used_fuel > self.fuel_tank_capacity:
            print(f"Not enough fuel to drive {kms_drove} KMs.\n"
                  f"Max KM you can drive: {self.fuel_tank_capacity * 100 / self.fuel_consumption} KM.\n"
                  f"Needed fuel to drive {kms_drove} KM: {used_fuel} L.\n")
        else:
            self.km += kms_drove
            self.fuel -= used_fuel
            print(f"KMs drove: {kms_drove} km, used fuel: {used_fuel} L\n")

    def fill_to_full(self):
        self.fuel = self.fuel_tank_capacity
        print('Tank filled to full.\n')

    def add_car_fix(self, year: int, fix: str):
        fix_list = self.fixes.get(year, [])
        fix_list.append(fix)
        self.fixes[year] = fix_list

    # PRINTS all fixes dictionary, RETURNS nada
    def show_all_fixes(self):
        print(f'Maintenance log for {self.manufacturer} {self.model}:')
        for k, v in self.fixes.items():
            print(f"Date: {k}, Fix: {v}")

    # RETURNS all fixes as a dict value, PRINTS nada
    def get_all_fixes(self) -> dict:
        return self.fixes

mazda_car = Car('Mazda', '3 Spirit', 'white',
                fuel_consumption=20, fuel_tank_capacity=60, year=2015)

toyota_car = Car('Toyota', 'Land Cruiser', 'white',
                 fuel_consumption=25, fuel_tank_capacity=40, year=2022)

# mazda_car.display_dashboard()
# mazda_car.fill_tank() - Best practice                     | That's why we use
# Car.fill_tank(mazda_car) - Not illegal, but bad practice  | 'self' (mazda_car) in Class methods

# mazda_car.fill_tank(20)
# mazda_car.display_dashboard()
# mazda_car.fill_tank(100)
# mazda_car.display_dashboard()

# mazda_car.drive(200)
mazda_car.fill_tank(60)
print('')
mazda_car.drive(24)
mazda_car.display_dashboard()
mazda_car.fill_to_full()
mazda_car.display_dashboard()
mazda_car.drive(301)
mazda_car.drive(290)
mazda_car.display_dashboard()
mazda_car.add_car_fix(2019, "New tires")
mazda_car.add_car_fix(2019, "Changed air filter")
mazda_car.add_car_fix(2020, "Replaced engine")
mazda_car.show_all_fixes()
print(mazda_car.get_all_fixes())
