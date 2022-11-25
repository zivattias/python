import random

import assignments.flight_ticket_program.utilities.consts
from assignments.flight_ticket_program.utilities.consts import *
import time

total_ticket_price = 0
flight_class = dict()
customer_name = str()

# Greetings function:
def greetings():
    print(WELCOME_MSG)
    time.sleep(3)
    print(f'\n' * 25)
    time.sleep(2)

# Retrieve customer name function:
def customer_info():
    global customer_name
    print(f'Welcome aboard. How should we call you?\n'
          f'Please enter your name.')
    first_name: str = input('>> FIRST NAME: ')
    last_name: str = input('>> LAST NAME: ')
    customer_name = first_name + " " + last_name

# Present flight details and ask to complete ticket assembly function:
def flight_info():
    print(f'We have found a relevant flight under your name, {customer_name}.\n'
          f'| FLIGHT DETAILS:\n'
          f'| 1. AIRLINE: {AIRLINE_NAME}\n'
          f'| 2. FLIGHT NUMBER: {FLIGHT_NUMBER}\n'
          f'| 3. ORIGIN: {ORIGIN}\n'
          f'| 4. DESTINATION: {DESTINATION}\n'
          f'| 5. PLANE: {AIRPLANE_NAME}\n'
          f'>> TO-DO: Complete ticket assembly')

    while True:
        ticket_assembly = input(f'>> Would you like to do that now, {customer_name}? '
                                f'[Y - Yes, N - No]: ').strip().lower()
        if ticket_assembly == 'y':
            return
        elif ticket_assembly == 'n':
            print(f"You chose to complete your ticket assembly another time.\n"
                  f"We'll be expecting you, {customer_name}!\n"
                  f"Bye-bye.")
            exit()
        else:
            print(f"Looks like you entered an illegal choice ('{ticket_assembly}').\n"
                  f"Let's try again!")

# Flight class suggestion menu. The function returns chosen class dictionary:
def choose_class():
    global flight_class
    print(f"In just a few simple steps you'll begin your journey from {ORIGIN}\n"
          f"to {DESTINATION}. Exciting!\n"
          f"Let's review our flight classes.")
    for i, c in enumerate(TICKET_CLASS):
        print(f">> {i+1}. {c}")

    while True:
        class_choice = input('>> CLASS: Please choose your preferred flight class '
                             'number (ex: enter 1 for First Class): ')
        match class_choice:
            case "1":
                flight_class = TICKET_CLASS['FIRST']
                seat_menu = flight_class['seat_layout']
                break
            case "2":
                flight_class = TICKET_CLASS['BUSINESS']
                seat_menu = flight_class['seat_layout']
                break
            case "3":
                flight_class = TICKET_CLASS['ECONOMY']
                seat_menu = flight_class['seat_layout']
                break
            case _:
                print(f'Invalid input ("{class_choice}"), try 1, 2 or 3!')
    print(seat_menu)

# Function to choose row and seats within flight class:
def choose_row_and_seat():
    global total_ticket_price
    print("Please choose your seat.")
    while True:
        row = input('>> ROW: Please choose your row: ')
        if not row.isdigit():
            print(f"ERROR: Use numbers.")
        else:
            row = int(row)
            if row not in flight_class["class_lines"]:
                print(f"ERROR: Row ('{row}') is not an available row.")
            else:
                break
    while True:
        seat = input('>> SEAT: Please choose your seat: ').upper()
        if seat not in flight_class["available_seats"]:
            print(f"ERROR: Seat ('{seat}') is not an available seat.")
        else:
            if seat in flight_class["window_seat"]:
                total_ticket_price += flight_class["class_seat_fee"]
                TICKET_BREAKDOWN['extra_seat_fee'] = flight_class["class_seat_fee"]
            break
    plane_seat = str(row) + seat
    print(f">> Your seat is: {plane_seat}, in {flight_class['class_name']}.")

    if flight_class["class_id"] == 1:
        total_ticket_price += 4000
        TICKET_BREAKDOWN["class_price"] = 4000
    elif flight_class["class_id"] == 2:
        if 5 <= row <= 7:
            total_ticket_price += 3000
            TICKET_BREAKDOWN["class_price"] = 3000
        else:
            total_ticket_price += 2300
            TICKET_BREAKDOWN["class_price"] = 2300
    elif flight_class["class_id"] == 3:
        if 11 <= row <= 20:
            total_ticket_price += 1700
            TICKET_BREAKDOWN["class_price"] = 1700
            if row == 12:
                total_ticket_price += 10
                TICKET_BREAKDOWN["extra_seat_fee"] += 10
        elif 21 <= row <= 40:
            total_ticket_price += 1400
            TICKET_BREAKDOWN["class_price"] = 1400
            if row == 22:
                total_ticket_price += 10
                TICKET_BREAKDOWN["extra_seat_fee"] += 10
        elif 41 <= row <= 60:
            total_ticket_price += 1200
            TICKET_BREAKDOWN["class_price"] = 1200
            if row == 42:
                total_ticket_price += 10
                TICKET_BREAKDOWN["extra_seat_fee"] += 10
    print(f"> AMOUNT DUE: ${total_ticket_price}\n")

# Function to choose available meal within flight class:
def choose_meal():
    global total_ticket_price

    print(f"Time to choose a meal for your flight, {customer_name}.\n"
          f"{flight_class['class_name']} is eligible for:")
    if flight_class["class_id"] == 1:
        print(f'> Chef meal (First Class) - FREE!\n')
    elif flight_class["class_id"] == 2:
        print(f'> Chef meal (First Class) for ${flight_class["upgrade_meal_fee"]["First"]}\n'
              f'> Business Class meal - FREE!')
    else:
        print(f'> Chef meal (First Class) for ${flight_class["upgrade_meal_fee"]["First"]}\n'
              f'> Business Class meal for ${flight_class["upgrade_meal_fee"]["Business"]}\n'
              f'> Economy Class meal for ${flight_class["upgrade_meal_fee"]["Economy"]}')

    while True:
        if flight_class["class_id"] != 1:
            chosen_meal = input('> Please choose your meal by typing its respective class (ex: First): ')\
                .strip().title()
            if chosen_meal not in flight_class["upgrade_meal_fee"]:
                print(f"ERROR: '{chosen_meal}' is not an available meal for you. Try again.")
            else:
                print(f"SUCCESS: {chosen_meal} Class meal has been added to your cart.")
                total_ticket_price += flight_class["upgrade_meal_fee"][f"{chosen_meal}"]
                TICKET_BREAKDOWN["meal_fee"] = flight_class["upgrade_meal_fee"][f"{chosen_meal}"]
                print(f"> AMOUNT DUE: ${total_ticket_price}\n")
                break
        else:
            chosen_meal = 'First'
            break
    if chosen_meal == 'First':
        print("There are multiple options for Gordon Ramsay's meal.")
        for i in LUXURY_MEAL_MENU:
            print(f"{i}. {LUXURY_MEAL_MENU[i]}")
        while True:
            course_id = int(input("> What course would you like? "))
            if course_id not in LUXURY_MEAL_MENU:
                print("ERROR: Unavailable meal number. Try again.")
            else:
                print(f'> FOOD: Meal #{course_id} has been added to your itinerary.')
                break


# Function to check customer's luggage weight and apply applicable fees:
def check_luggage():
    global total_ticket_price
    print(f">> LUGGAGE GUIDELINES: Dear {customer_name},\n"
          f"\tAccording to your class ({flight_class['class_name']}),\n"
          f"\tyour maximum luggage capacity is: {flight_class['maximum_luggage_weight']}.")
    while True:
        weight = input(f"> LUGGAGE FEE: Please insert your luggage weight (kg): ")
        if not weight.isdigit():
            print("ERROR: Weight can be inserted in numbers only.")
        else:
            weight = int(weight)
            break

    luggage_fee = 0
    if flight_class["class_id"] == 3 or flight_class["class_id"] == 2:
        if weight > flight_class["maximum_luggage_weight"]:
            luggage_fee = (weight - flight_class["maximum_luggage_weight"]) / 10 * flight_class["luggage_fee"]
            print(f"> LUGGAGE FEE ADDED: ${luggage_fee}")
        else:
            print("> NO LUGGAGE FEE ADDED.")
    total_ticket_price += luggage_fee
    TICKET_BREAKDOWN["luggage_fee"] = luggage_fee
    print(f"> AMOUNT DUE: ${total_ticket_price}\n")

def ticket_breakdown():
    fare_breakdown_list: list = assignments.flight_ticket_program.utilities.consts.TICKET_BREAKDOWN
    print(f"""
            PYLINES PRICE BREAKDOWN:
          | ORIGIN: {ORIGIN}
          | DESTINATION: {DESTINATION}        
          | NAME: {customer_name}
          | CLASS: {TICKET_BREAKDOWN['class_price']}
          | EXTRA SEAT FEES: {TICKET_BREAKDOWN['extra_seat_fee']}
          | MEAL PRICE: {TICKET_BREAKDOWN['meal_fee']}
          | LUGGAGE FEE: {TICKET_BREAKDOWN['luggage_fee']}
          |####################
          | TOTAL DUE: {total_ticket_price}
          |####################\n
          """
          )

def lottery():
    global total_ticket_price
    print(f">> LOTTERY: Welcome to Pylines' lottery system, where you could earn a discount for your ticket!")
    while True:
        num = input('Please enter a number ranging from 1 to 9 (inclusive): ')
        if not num.isdigit():
            print('Oops! Wrong input. Pay attention to digits.')
        else:
            num = int(num)
            if not 1 <= num <= 9:
                print('Oops! Wrong input. Pay attention to range.')
            else:
                print(f'>> LOTTERY: Your number is: {num}.')
                break

    name_len = len("".join(customer_name.split(" ")))
    remainder = name_len * random.randint(1, 5) % num
    if remainder <= 5:
        print(f'> YOU WON: You got a %{remainder} discount!')
        total_ticket_price = (100 - remainder) * total_ticket_price / 100
        print(f'> Discounted ticket price: {total_ticket_price}')
    else:
        print("> Try again next time! Bye-bye.")
        exit()


def flow():
    # greetings()
    customer_info()
    flight_info()
    choose_class()
    choose_row_and_seat()
    choose_meal()
    check_luggage()
    ticket_breakdown()
    lottery()