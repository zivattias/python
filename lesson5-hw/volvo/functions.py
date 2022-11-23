from consts import *

def print_layout(_d: dict, sep: str) -> str:
    layout = ""
    for k, v in _d.items():
        layout += f"{k}{sep} {v}\n"
    return layout

def menu():
    menu_option = input(f"Welcome to Volvo's Catalog!\n"
                        f"What would you like to do?"
                        f"{print_layout(MENU_OPTIONS, sep='.')}")
    return menu_option

def new_car():
    car_type = input(f"\nEnter the vehicle's type:\n"
                     f"{print_layout(VEHICLE_TYPES, sep='.')}\n"
                     f">>> ")
    if car_type == 1:
        model_dict = MODEL_PRIVATE
    else:
        model_dict = MODEL_SEMI
    car_year = input(f"\nEnter the vehicle's year:"
                     f">>> ")
    car_engine = input(f"\nEnter the vehicle's engine type:\n"
                       f"{print_layout(ENGINE_TYPE, sep='.')}\n"
                       f">>> ")
    car_color = input(f"\nEnter the vehicle's color:\n"
                      f"{print_layout(VEHICLE_COLORS, sep='.')}\n"
                      f">>> ")
    car_model = input(f"\nEnter vehicle's model:\n"
                      f"f{print_layout(model_dict, sep='.')}\n"
                      f">>> ")
    car = dict()
    car["vehicle_type"] = car_type
    car["production_year"] = car_year
    car["engine_type"] = car_engine
    car["vehicle_color"] = car_color
    car["model_type"] = car_model
    return car

