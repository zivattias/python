# START

ORIGIN = 'Ben Gurion Intl, Tel Aviv'

DESTINATION = 'John F Kennedy, New York City'

FLIGHT_CHEF = 'Gordon Ramsay'

AIRPLANE_NAME = 'Boeing 747-8 VIP'

AIRLINE_NAME = 'Pylines'

FLIGHT_NUMBER = 'PY2308'

WELCOME_MSG = f'''
                             _ .                         
                           (  _ )_                      
                         (_  _(_ ,)
                    
                       __|__
                --@--@--(_)--@--@--
          _  _
         ( `   )_
        (    )    `)                
      (_   (_ .  _) _)
      
      
            Thank you for choosing {AIRLINE_NAME}!
                We hope to provide the best
                    airline experience
                        for you.
            
      
                                     _
                                    (  )
     _ .                         ( `  ) . )
   (  _ )_                      (_, _(  ,_)_)
 (_  _(_ ,)
'''

TICKET_CLASS = {
    'FIRST': {
        "class_id": 1,
        "class_name": "First Class",
        "class_price": 4000,
        "class_lines": [1, 2, 3, 4],
        "class_seat_fee": 0,
        "maximum_luggage_weight": "unlimited",
        "window_seat": ['A', 'D'],
        "available_seats": ['A', 'B', 'C', 'D'],
        "luggage_fee": 0,
        "upgrade_meal_fee": {
            'First': 0
        },
        "seat_layout": '''
        ----------------<FIRST CLASS SEAT MAP>-------------------
        | PLACE: | WINDOW     AISLE   |    AISLE      WINDOW     |
        | PRICE: | $4,000     $4,000  |    $4,000     $4,000     |
        | ROW: 1 |    A         B     |      C           D       |
        | ROW: 2 |    A         B     |      C           D       |
        | ROW: 3 |    A         B     |      C           D       |
        | ROW: 4 |    A         B     |      C           D       |
        ---------------------------------------------------------
        '''
    },
    'BUSINESS': {
        "class_id": 2,
        "class_name": "Business Class",
        # Lines 5-7, 3000 | Lines 8-10, 2300
        "class_price": (3000, 2300),
        "class_lines": [5, 6, 7, 8, 9, 10],
        # The seat fee is applicable for seats A and D only
        "class_seat_fee": 55,
        "window_seat": ['A', 'D'],
        "available_seats": ['A', 'B', 'C', 'D'],
        # The luggage fee is applicable for each kg if exceeds 50kg
        "maximum_luggage_weight": 50,
        "luggage_fee": 10,
        "upgrade_meal_fee": {
            'First': 42,
            'Business': 0
        },
        "seat_layout": '''
        ----------------<BUSINESS CLASS SEAT MAP>----------------
        | PLACE: | WINDOW     AISLE       AISLE      WINDOW     |
        | PRICE: | $3,055     $3,000      $3,000     $3,055     |
        | ROW: 5 |    A         B           C           D       |
        | ROW: 6 |    A         B           C           D       |
        | ROW: 7 |    A         B           C           D       |
        | PRICE: | $2,355     $2,300      $2,300     $2,355     |
        | ROW: 8 |    A         B           C           D       |
        | ROW: 9 |    A         B           C           D       |
        | ROW: 10|    A         B           C           D       |
        ---------------------------------------------------------
        '''
    },
    'ECONOMY': {
        "class_id": 3,
        "class_name": "Economy Class",
        # Lines 11-20, 1700 | Lines 21-40, 1500 | Lines 41-60, 1200
        "class_price": (1700, 1500, 1200),
        "class_lines": [11, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 23, 24, 25, 26, 27, 28, 29, 30,
                        31, 32, 33, 34, 35, 36, 37, 38, 39,
                        40, 41, 43, 44, 45, 46, 47, 48, 49,
                        50, 51, 52, 53, 54, 55, 56, 57, 58,
                        59, 60, 12, 22, 42],
        # "extra_room_lines": [12, 22, 42]
        # The line fee is applicable for lines 12, 22 and 42 as 'extra room fee'
        "class_lines_fee": 10,
        # The seat fee is applicable for seats A and F only
        "class_seat_fee": 10,
        "window_seat": ['A', 'F'],
        "available_seats": ['A', 'B', 'C', 'D', 'E', 'F'],
        # The luggage fee is applicable for each kg if exceeds 20kg
        "maximum_luggage_weight": 20,
        "luggage_fee": 10,
        "upgrade_meal_fee": {
            'First': 42,
            'Business': 22,
            'Economy': 7
        },
        "seat_layout": '''
         ----------------------------<ECONOMY CLASS SEAT MAP>--------------------------
        | >> (E) means extra leg room that is purchasable for extra $10 along with     |
        |    window fees, for applicable seats.                                        |
        |______________________________________________________________________________|
        | PLACE:     | WINDOW     MIDDLE     AISLE     AISLE     MIDDLE     WINDOW     |
        |------------------------------------------------------------------------------|
        | PRICE:     | $1,710     $1,700    $1,700   $1,700     $1,700    $1,710       |
        | ROW: 11-20 |    A         B         C         D         E         F          |
        | ROW: 12(E) |    A(+$10)   B(+$10)   C(+$10)   D(+$10)   E(+$10)   F(+$10)    |
        |------------------------------------------------------------------------------|
        | PRICE:     | $1,410     $1,400    $1,400   $1,400     $1,400    $1,410       |
        | ROW: 21-40 |    A         B         C         D         E         F          |
        | ROW: 22(E) |    A(+$10)   B(+$10)   C(+$10)   D(+$10)   E(+$10)   F(+$10)    |
        |------------------------------------------------------------------------------|
        | PRICE:     | $1,210     $1,200    $1,200   $1,200     $1,200    $1,210       |
        | ROW: 41-60 |    A         B         C         D         E         F          |
        | ROW: 42(E) |    A(+$10)   B(+$10)   C(+$10)   D(+$10)   E(+$10)   F(+$10)    |
         ------------------------------------------------------------------------------
        '''
    }
}

LUXURY_MEAL_MENU = {
    1: ' STARTER - Roast veal sweetbread\n'
       '\tMAIN - Cornish turbot\n'
       '\tDESERT  - Hazelnut souffle\n',
    2: ' STARTER - Ravioli lobster\n'
       '\tMAIN - 100-Day aged Cambrian Blue Grey\n'
       '\tDESERT - Pecan praline\n',
    3: ' STARTER - Scallops from the Isle of Skye\n'
       '\tMAIN - Aynhoe Park fallow deer\n'
       '\tDESERT - Caramelised apple Tarte tatin\n'
}

TICKET_BREAKDOWN = {
    "class_price": 0,
    "extra_seat_fee": 0,
    "meal_fee": 0,
    "luggage_fee": 0
}


# END