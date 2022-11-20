#Greetings

#We need to return ticket price and the description of the order

#Choose class - First, Business, Economy
    #if [F] -> ticket_price = $4000

#Choose Line
    #If [F] -> lines 1-4

    #If [B] -> lines 5-7 ==> ticket_price = $3000
    #If [B] -> lines 8-10 ==> ticket_price = $2300

    #If [E] -> lines 11-20 ==> ticket_price = $1700
    #If [E] -> lines 21-40 ==> ticket_price = $1500
    #If [E] -> lines 41-60 ==> ticket_price = $1200

#Choose Seats
    #if [F] -> seats [A][B][C][D] -> [A][D] are window

    #if [B] -> seats [A][B][C][D] -> [A][D] are window ==> ticket_price + $55

    #if [E] -> seats [A][B][C][D][E][F] -> [A][F] are window ==> ticket_price + $10
    #if [E] + Line [12,22,42] -> seats with extra leg room  ==> ticket_price + $15

#Choose Luggage
    #if [F] -> no change

    #if [B] -> if (luggage > 50kg)  ==> ticket_price + $10/kg

    #if [E] -> if (luggage > 20kg)  ==> ticket_price + $10/kg

#Choose Meal
    #if [F] -> meal menu ->no change in price

    #if [B] -> meal menu -> if luxury ==> ticket_price + $42
    #if [B] -> meal menu -> if business ==> no change in price

    # if [E] -> meal menu + no meal option-> if luxury ==> ticket_price + $42
    # if [E] -> meal menu + no meal option -> if business ==> ticket_price + $22
    # if [E] -> meal menu + no meal option -> if luxury ==> ticket_price + $7

#Lotery
from random import randrange

first_name = 'John'
last_name = 'Doe'

ticket_price = 0
flight_class = 'E' # the basic ticket is economy class

# the basic meal is no meal. There will be 4 meal menus.
# meal = 0 - no meal
# meal = 1 - economy -> +$7
# meal = 2 - business -> +$22
# meal = 3 - first class -> +$42


meal_menu_1 = '' # in luxury meal there are 3 menus
window_extra ='+ $0'
luggage_extra ='+ $0'
leg_room_extra = '+ $0'
meal_type = ''
meal_extra ='+ $0'
chef_meal_menu = '-'


# You can also COPY & PASTE the symbol from the table . Copy this symbols: ► ▲ ◄ ▼ ☼ ♫ ▄ ◙ ░
# New for you: How to add a special characters ==> https://stackoverflow.com/questions/37130884/how-to-display-the-arrow-symbol-in-python-tkmessagebox
# Special character : smile ==> \u263a
# List of special characters ==>  https://python-tcod.readthedocs.io/en/latest/tcod/charmap-reference.html

print(f"#########################################################################################\n"
      f"\t\t\t\tWelcome to NYT Airlines.\n"
      f"\t\t\t\tWe are happy to have you here \u263a\n"
      f"#########################################################################################\n\n"
      f"Let's book a flight ticket for you!\n\n"
      f"Please enter your name")

first_name = input("\t>> First name : ")
if not first_name.isalpha():
    print(f"\t\t∟   Wrong input : First name = [{first_name}] :(\n"
          f"\t\t    'First name' should include letters only.\n")
    first_name = input("\t>> First name : ")
    if not first_name.isalpha():
        print(f"\t\t∟   Wrong input : First name = [{first_name}] :(\n"
              f"\t\t    Can't proceed without a real name.\n"
              f"\n"
              f"\t\t    RESTART the program\n")
        exit()

last_name = input("\t>> Last name : ")
if not last_name.isalpha():
    print(f"\t\t∟   Wrong input : Last name = [{last_name}] :(\n"
          f"\t\t    'Last name' should include letters only.\n")
    first_name = input("\t>> First name : ")
    if not last_name.isalpha():
        print(f"\t\t∟   Wrong input : First name = [{last_name}] :(\n"
              f"\t\t    Can't proceed without a real name.\n"
              f"\n"
              f"\t\t    RESTART the program\n")
        exit()



print(f"\t\t∟ It's a lovely day {first_name} {last_name} !\n\n"
      f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      f"Please choose desired flight class for your journey:\n"
      f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      f"░\tTicket Class                             ║\tPrice Range                         ░\n"
      f"░\t══════════════════════════               ║\t══════════════════════════          ░\n"
      f"░\t[F] for FIRST class                      ║\t$4,000                              ░\n"
      f"░\t[B] for BUSINESS class                   ║\t$2,300 - $3,000                     ░\n"
      f"░\t[E] for ECONOMY class                    ║\t$1,200 - $1,700                     ░\n"
      f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

flight_class = input(f"\t>> Input letter here: ").upper()

if (flight_class!='F') and (flight_class!='B') and (flight_class!='E'):

      print(f"\t\t  ∟ Dear {first_name} {last_name} you've entered a wrong input: [{flight_class}]\n"
            f"\t\t\tWe hope next time you'll have a better luck.\n"
            f"\t\t\tBut for now, the program exits.\n\n"
            f"\t\t\t♦♦♦ GOOD LUCK ♦♦♦")
      exit()



#Chose Seats
#####################
      #Seat
if flight_class=='F':
    flight_class_type = 'First'
    print(f"\n"
            f"Window or aisle seat plane?\n"
            f"Chose [A] or [D] for a window seat or if you wish to seat near aisle chose [B] or [C]\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            f"░\t                   CABIN                        ║                                ░\n"
            f"░\t  ═════════════════════════════════════════════ ║  ═══════════════════════════   ░\n"
            f"░\t               FIRST CLASS                      ║              Price             ░\n"
            f"░\t Window            Aisle          Window  Line  ║    Base      Window   Ex.leg   ░\n"
            f"░\t      ▌  [A]  [B]  │   │ [C] [D]  ▐       1     ║    $4,000      -        -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │ [C] [D]  ▐       2     ║    $4,000      -        -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │ [C] [D]  ▐       3     ║    $4,000      -        -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │ [C] [D]  ▐       4     ║    $4,000      -        -      ░\n"
            f"░\t  ═════════════════════════════════════════════ ║                                ░\n"
            f"░\t               BUSINESS CLASS                   ║                                ░\n"
            f"░\t      ▌  [A]  [B]  │   │ [C] [D]  ▐       5     ║                                ░\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
elif flight_class=='B':
    flight_class_type = 'Business'
    print(f"\n"
            f"Window or aisle seat plane?\n"
            f"Chose [A] or [D] for a window seat or if you wish to seat near aisle chose [B] or [C]\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            f"░\t                   CABIN                        ║                                ░\n"
            f"░\t  ═════════════════════════════════════════════ ║                                ░\n"
            f"░\t               FIRST CLASS                      ║              Price             ░\n"
            f"░\t  ═════════════════════════════════════════════ ║  ═══════════════════════════   ░\n"
            f"░\t               BUSINESS CLASS                   ║                                ░\n"
            f"░\t Window            Aisle            Window  Line║    Base      Window   Ex.leg   ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       5   ║    $3,000    +$55       -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       6   ║    $3,000    +$55       -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       7   ║    $3,000    +$55       -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       8   ║    $2,300    +$55       -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       9   ║    $2,300    +$55       -      ░\n"
            f"░\t      ▌  [A]  [B]  │   │  [C]  [D]  ▐       10  ║    $2,300    +$55       -      ░\n"
            f"░\t  ═════════════════════════════════════════════ ║                                ░\n"
            f"░\t               ECONOMY CLASS                    ║                                ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       11  ║                                ░\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
else:
    flight_class_type = 'Economy'
    print(f"\n"
            f"Window or aisle seat plane?\n"
            f"Chose [A] or [F] for a window seat or if you wish to seat near aisle chose [C] or [D]\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            f"░\t                   CABIN                        ║                                ░\n"
            f"░\t  ═════════════════════════════════════════════ ║                                ░\n"
            f"░\t                FIRST CLASS                     ║                                ░\n"
            f"░\t  ═════════════════════════════════════════════ ║                                ░\n"
            f"░\t              BUSINESS CLASS                    ║              Price             ░\n"
            f"░\t  ═════════════════════════════════════════════ ║  ═══════════════════════════   ░\n"
            f"░\t               ECONOMY CLASS                    ║                                ░\n"
            f"░\t Window            Aisle            Window  Line║    Base      Window   Ex.leg   ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       11  ║    $1,700    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       12  ║    $1,700    +$10      +$15    ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       13  ║    $1,700    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,700    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,700    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       20  ║    $1,700    +$10       -      ░\n"
            f"░\t                                                ║                                ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       21  ║    $1,500    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       22  ║    $1,500    +$10      +$15    ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       23  ║    $1,500    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,500    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,500    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       40  ║    $1,500    +$10       -      ░\n"
            f"░\t                                                ║                                ░\n"
            f"░\t                                                ║                                ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       41  ║    $1,200    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       42  ║    $1,200    +$10      +$15    ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       43  ║    $1,200    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,200    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       .   ║    $1,200    +$10       -      ░\n"
            f"░\t      ▌[A] [B] [C] │   │ [D] [E] [F]▐       60  ║    $1,200    +$10       -      ░\n"
            f"░\t                                                ║                                ░\n"
            f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
seat_input = input("\t>> Input desired seat in format [#line][seat] (Ex: 8B): ")
seat_col = seat_input[-1].upper()
seat_row_input = seat_input[:-1]

if not seat_col.isalpha(): # Check if seat is NOT a single letter
    seat = None
else:
    seat = seat_col

if not seat_row_input.isnumeric(): # Check if input row info is NOT a number
    seat_row = None #in any case this is wrong input, but further it will cut
else:
    seat_row = int(seat_row_input)

if flight_class == 'F':
    #check the First class first
    ticket_price = 4000 #this is the final price for the First class
    ticket_basic_price = ticket_price
    if seat==None or seat<'A' or seat>'D': #check if seats are out of range
        print(f"\t\t∟   Wrong input : seat = [{seat}] :(\n"
              f"\t\t    First class includes [A],[B],[C] and [D] only.\n")
        seat = 'A' #chose some option
        print(f"\t\t∟   Don't worry, we got the perfect place for you. It will be column [{seat}].\n")
    if seat_row== None or seat_row<1 or seat_row>4: #check if row number is out of range
        print(f"\t\t∟   Wrong input : seat row = [{seat_row}] :(\n"
              f"\t\t    First class' rows are 1-4 included.\n")
        seat_row = 2 #chose some option
        print(f"\t\t    We choose the best row for you: [{seat_row}].\n")

    #print the chosen seat
    print(f"\t\t∟   It's a perfect pick!\n"
          f"\t\t    The chosen seat is: {seat_row}{seat.upper()}.\n")

elif flight_class == 'B':
    # check the business class
    if seat == None or seat < 'A' or seat > 'D':  # check if seats are out of range
        print(f"\t\t∟   Wrong input : seat = [{seat}] :(\n"
              f"\t\t    Business class includes seats from [A] to [D] only.\n")
        seat = 'B'  # chose some option
        print(f"\t\t∟   Don't worry, we got the perfect place for you. It will be column [{seat}].\n")
    if seat_row== None or seat_row < 5 or seat_row > 10:  # check if row number is out of range
        print(f"\t\t∟   Wrong input : seat row = [{seat_row}] :(\n"
              f"\t\t    Business class' rows are 5-10 included.\n")
        seat_row = 10  # chose some option
        print(f"\t\t    We choose the best row for you: [{seat_row}].\n")

    # print the chosen seat
    print(f"\t\t∟   It's a perfect pick!\n"
          f"\t\t    The chosen seat is: {seat_row}{seat.upper()}.\n")

    #Checking the ticket price
    #If [B] -> lines 5-7 ==> ticket_price = $3000
    #If [B] -> lines 8-10 ==> ticket_price = $2300
    if seat_row>=5 and seat_row<=7:
        ticket_price = 3000
    else:
        ticket_price = 2300
    ticket_basic_price = ticket_price

    if seat=='A' or seat=='D': #seats near the window costs extra $55
        window_extra = '+ $55'
        ticket_price=ticket_price+55

else:
    # check the Economy class
    if seat == None or seat < 'A' or seat > 'F':  # check if seats are out of range
        print(f"\t\t∟   Wrong input : seat = [{seat}] :(\n"
              f"\t\t    Economy class includes seats from [A] to [F] only.\n")
        seat = 'E'  # chose some option
        print(f"\t\t∟   Don't worry, we got the perfect place for you. It will be column [{seat}].\n")
    if seat_row== None or seat_row < 11 or seat_row > 60:  # check if row number is out of range
        print(f"\t\t∟   Wrong input : seat row = [{seat_row}] :(\n"
              f"\t\t    Economy class' rows are 11-60 included.\n")
        seat_row = 60  # chose some option
        print(f"\t\t    We choose the best row for you: [{seat_row}].\n")

    # print the chosen seat
    print(f"\t\t∟   It's a perfect pick!\n"
          f"\t\t    The chosen seat is: {seat_row}{seat.upper()}.\n")

    # Checking the ticket price
    #If [E] -> lines 11-20 ==> ticket_price = $1700
    #If [E] -> lines 21-40 ==> ticket_price = $1500
    #If [E] -> lines 41-60 ==> ticket_price = $1200
    if seat_row >= 11 and seat_row <= 20:
        ticket_price = 1700
    elif seat_row >= 21 and seat_row <= 40:
        ticket_price = 1500
    else:
        ticket_price = 1200
    ticket_basic_price = ticket_price

    # if [E] -> seats [A][B][C][D][E][F] -> [A][F] are window ==> ticket_price + $10
    if seat == 'A' or seat == 'F':
        window_extra ='+ $10'
        ticket_price = ticket_price + 10

    #if [E] + Line [12,22,42] -> seats with extra leg room  ==> ticket_price + $15
    if seat_row == 12 or seat_row == 22 or seat_row == 42:  # seats near the window costs extra $10
        ticket_price = ticket_price + 15
        leg_room_extra = '+ $15'

#Choose Luggage
    #if [F] -> no change

    #if [B] -> if (luggage > 50kg)  ==> ticket_price + $10/kg

    #if [E] -> if (luggage > 20kg)  ==> ticket_price + $10/kg
luggage_weight_input = input("\t>> Input your luggage weight in [kg]: ")

#check the input and if wrong ask again once
if not luggage_weight_input.isnumeric() or int(luggage_weight_input)<0:
    print(f"\t\t∟   Wrong input : [{luggage_weight_input}] :(\n"
          f"\t\t    Your input should include positive number only.\n")
    luggage_weight_input = input("\t>> Input your luggage weight in (kg). Positive digits only: ")
    if not luggage_weight_input.isnumeric() or int(luggage_weight_input) < 0: #check second time
        print(f"\t\t∟   Wrong input : [{luggage_weight_input}] :(\n")
        if flight_class == 'F':
            print(f"\t\t    It was a long day, Let's pretend your luggage weights 60 (kg).\n"
                  f"\t\t    Because you have a FIRST class.\n")
        else:
            print(f"\t\t    It looks like you are trying to cheat us...\n"
                  f"\t\t    Let me guess, your luggage weights ~80(kg). Definitely!\n"
                  f"\t\t    So sorry, you'll have to pay extra $10 for every extra (kg).\n")
            weight = 80
else:
    weight = int(luggage_weight_input)

#if [Business] -> if (luggage > 50kg)  ==> ticket_price + $10/kg
if flight_class == 'B' and weight>50:
    luggage_extra = '+ $'+str((weight-50)*10)
    ticket_price = ticket_price + (weight-50)*10
    print(f"\t\t∟   Looks like your luggage weights  additional {weight-50}(kg) from the resereved 50(kg) :(\n"
          f"\t\t    You'll be charged additional ${(weight-50)*10}.\n")

elif flight_class == 'E' and weight>20:
    luggage_extra = '+ $' + str((weight - 20) * 10)
    ticket_price = ticket_price + (weight-20)*10
    print(f"\t\t∟   Looks like your luggage weights  additional {weight-20}(kg) from resereved 20(kg) :(\n"
          f"\t\t    You'll be charged additional ${(weight-20)*10}.\n")

#Choose Meal
    #if [F] -> meal menu ->no change in price

    #if [B] -> meal menu -> if luxury ==> ticket_price + $42
    #if [B] -> meal menu -> if business ==> no change in price

    # if [E] -> meal menu + no meal option-> if luxury ==> ticket_price + $42
    # if [E] -> meal menu + no meal option -> if business ==> ticket_price + $22
    # if [E] -> meal menu + no meal option -> if luxury ==> ticket_price + $7

chef_meal =False # if Business or Economy will choose the Luxury meal it will chage to True
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      f"We are almost there. Let's chose a meal for you.\n\n")

if flight_class == 'E':
    print(f"{first_name} {last_name} let's bring some taste to your flight !\n"
          f"Please choose the desired type of meal:\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
          f"░\t[0] No meal                  → $0                                               ░\n"
          f"░\t[1] Economy meal             → $7                                               ░\n"
          f"░\t[2] Business meal            → $22                                              ░\n"
          f"░\t[3] Luxury meal, from chef   → $42                                              ░\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    meal_type_input = input("\t>> Insert meal number: ")
    if not meal_type_input.isnumeric() or int(meal_type_input)<0 or int(meal_type_input)>3:
        print(f"\t\t∟   Wrong input : [{meal_type_input}] :(\n"
              f"\t\t    Your input should include positive number only from 0 to 3.\n"
              f"\t\t    No second chance this time. You'll have an Economy meal for an extra $7. Enjoy! :-)\n")
        ticket_price = ticket_price +7
        meal_extra = '+ $7'
    else:
        meal_num = int(meal_type_input)
        if meal_num==0:
            print(f"\t\t∟   Great choice! Take a sandwich with you!\n")
            meal_type='No meal'
        elif meal_num==1:
            print(f"\t\t∟   You'll get an extraordinary sandwich from us!\n")
            ticket_price+=7
            meal_type = 'Economy meal'
            meal_extra = '+ $7'
        elif meal_num==2:
            print(f"\t\t∟   Business lunch is a very tasty meal indeed!\n")
            ticket_price+=22
            meal_type = 'Business meal'
            meal_extra = '+ $22'
        elif meal_num == 3:
            print(f"\t\t∟   OMG, no way... It will blow your mind :-)\n")
            ticket_price += 42
            meal_type = 'Luxury meal, from chef'
            meal_extra = '+ $42'
            chef_meal = True #ask to show the menu for the Luxury meal
#Meal pick for Business class pasanger
elif flight_class == 'B':
    print(f"{first_name} {last_name} let's bring some taste to your flight !\n"
          f"Please choose the desired type of meal:\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
          f"░\t[1] Business meal            → $22                                              ░\n"
          f"░\t[2] Luxury meal, from chef   → $42                                              ░\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    meal_type_input = input("\t>> Insert meal number: ")
    if not meal_type_input.isnumeric() or int(meal_type_input)<1 or int(meal_type_input)>2:
        print(f"\t\t∟   Wrong input : [{meal_type_input}] :(\n"
              f"\t\t    Your input should include positive number only from 1 to 2.\n"
              f"\t\t    We want you to have a second chance to choose your meal :-)\n\n")

        #second chance to choose the right meal
        print(f"\t\t∟ Don't mess this time !\n\n"
              f"Please choose the desired type of meal:\n"
              f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
              f"░\t[1] Business meal            → $22                                              ░\n"
              f"░\t[2] Luxury meal, from chef   → $42                                              ░\n"
              f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
        meal_type_input = input("\t>> Insert meal number: ")
        if not meal_type_input.isnumeric() or int(meal_type_input) < 1 or int(meal_type_input) > 2:
            print(f"\t\t∟   Wrong input : [{meal_type_input}] :(\n"
                  f"\t\t    Your input should include positive number only from 1 to 2.\n"
                  f"\t\t    Let's take the Business meal\n")
        ticket_price = ticket_price +22
        meal_type = 'Business meal'
        meal_extra = '+ $22'
    else:
        meal_num = int(meal_type_input)
        if meal_num==1:
            print(f"\t\t∟   Business lunch is a very tasty meal indeed!\n")
            ticket_price+=22
            meal_type = 'Business meal'
            meal_extra = '+ $22'
        elif meal_num == 2:
            print(f"\t\t∟   OMG, no way... It will blow your mind :-)\n")
            ticket_price += 42
            meal_type = 'Luxury meal, from chef'
            meal_extra = '+ $42'
            chef_meal = True #ask to show the menu for the Luxury meal

if flight_class == 'F' or chef_meal:
    meal_type = 'Luxury meal, from chef'
    print(f"Gordon Ramsay is going to cook for you on this flight.\n"
          f"We have a wonderful 3 menu, let's chose the best fit for you:\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
          f"░  [1] STARTER - Roast veal sweetbread                                             ░\n"
          f"░      MAIN    - Cornish turbot                                                    ░\n"
          f"░      DESERT  - Hazelnut souffle                                                  ░\n"
          f"░                                                                                  ░\n"
          f"░  [2] STARTER - Ravioli lobster                                                   ░\n"
          f"░      MAIN    - 100-Day aged Cumbrian Blue Grey                                   ░\n"
          f"░      DESERT  - Pecan praline                                                     ░\n"
          f"░                                                                                  ░\n"
          f"░  [3] STARTER - Scallops from the Isle of Skye                                    ░\n"
          f"░      MAIN    - Aynhoe Park fallow deer                                           ░\n"
          f"░      DESERT  - Caramelised apple Tarte Tatin                                     ░\n"
          f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    meal_input = input("\t>> Insert meal number: ")

    # Need to check if input is correct , e.i contains digits only and only from 1 to 3
    # If user inputs floating number (3.15) we'll cust it into integer (3)
    if not meal_input.isnumeric():
        chef_meal_num = 3
        print(f"\t\t∟ Wrong input : [{meal_input}] :(\n"
              f"\t\t\t You should chose meal number between 1 and 3 included.\n"
              f"\t\t\t However,Mr Ramsay says Scallops are wonderful today and he suggest you to go with meal # {chef_meal_num} for this time.\n")
    else:
        # saving {seat_line} once so we don't need to calculate {int(seat_line_input)} 3 times
        chef_meal_num = int(meal_input)
        if chef_meal_num > 0 and chef_meal_num < 4:
            # The input is number and is in range
            print(f"\t\t∟ You are a gourmet!\n"
                  f"\t\t\t The chosen meal menu is: #{chef_meal_num}.\n")
        else:
            # The input is number but out of the possible line range
            print(f"\t\t∟ We wish we had this number [{chef_meal_num}] in our menue.\n"
                  f"\t\t\t Let's go for a veal, it looks a great choice for you. The meal #1")
            chef_meal_num = 1
    if chef_meal_num == 1:
        chef_meal_menu = 'STARTER - Roast veal sweetbread , MAIN    - Cornish turbot,  DESERT  - Hazelnut souffle '
    elif chef_meal_num == 2:
        chef_meal_menu = 'STARTER - Ravioli lobster , MAIN    - 100-Day aged Cumbrian Blue Grey,  DESERT  - Pecan praline '
    else:
        chef_meal_menu = 'STARTER - Scallops from the Isle of Skye , MAIN    - Aynhoe Park fallow deer,  DESERT  - Caramelised apple Tarte Tatin '

#Print results
print(f"\n\n"
      f"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n\n"
      f"\t YOUR ORDER\n"
      f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
      f"░\tType                    ║\tSelected                                     \n"
      f"░\t════════════════════════════════════════════════════════════════════════════════\n"
      f"░\tTicket Class            ║\t{flight_class_type} → $ {ticket_basic_price}                 \n"
      f"░\tSeat                    ║\t{seat_row}{seat}                       \n"
      f"░\t                        ║\tExtra window seat  →  {window_extra}\n"
      f"░\t                        ║\tExtra leg room     →  {leg_room_extra}\n"
      f"░\tLuggage Weight          ║\t{weight}(kg)\n"
      f"░\t                        ║\tOverweight fee     →  {luggage_extra}\n"
      f"░\tMeal                    ║\tMeal_type →  {meal_type}\n"
      f"░\t                        ║\tAdd. fee  →  {meal_extra}\n"
      f"░\t                        ║\tMenu      →  {chef_meal_menu}\n"
      f"░\t════════════════════════════════════════════════════════════════════════════════\n"
      f"░\tTotal                   ║\t$ {ticket_price}                 \n"
      f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\n"
      f"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")


########################
#Bonus

discount_ans = input(f"Would you like to have a discount? (Y/N): ")
if discount_ans.lower()!='y':
    print(f"\t\t∟ There was no sign you'd like to have a discount, so the program exits.")
    exit()
else:
    name_length = len(first_name) + len(last_name)
    rand_number = randrange(1, 5)
    lucky_number = input("Input lucky number from 1 to 9 : ")
    if lucky_number.isalpha() or int(lucky_number) < 1 or int(lucky_number) > 9:
        print(f"\t\t∟ Wrong input: [{lucky_number}].\n"
              f"\t\t\t No second chance. Bey!")
        exit()

    remaining = int((name_length * rand_number) % int(lucky_number))
    if remaining > 5 and remaining == 0:
        print(f"You not win any discount")
    else:
        print(f"Congrats!!! You win {remaining}% discount\n"
              f"Ticket price after discount: ${int(ticket_price * (1 - remaining / 100))}")