from table_system import TableReservationSystem
from table_system_exceptions import *

def onGuestsArrived(guests_num):
    available_tables = japanika.get_available_tables(guests_num)
    if len(available_tables) == 0:
        print("No available tables, checking when the soonest table will become available...")
        next_available = japanika.get_soonest_available_tables(guests_num)
        print(f"The next available table is {next_available[0]}, will be available in {next_available[0].time_left()}")
        return None
    else:
        print(f"Available tables in Japanika for {guests_num} persons: {available_tables}")
        table_id_to_reserve = available_tables[0].table_id
        print(f"Reserving table {table_id_to_reserve} for {guests_num} persons")
        print(f"Reserved: {japanika.reserve(guests_num, table_id_to_reserve)}")
        return table_id_to_reserve

if __name__ == '__main__':
    # create a system for japanikao
    japanika = TableReservationSystem([3, 5, 2, 2, 6, 4, 3, 6], 'Japanika')

    try:
        japanika.reserve(10, 2)
    except TableException as e:
        print(e)

    try:
        japanika.reserve(2, 2)
    except TableException as e:
        print(e)

    try:
        japanika.reserve(2, 2)
    except TableException as e:
        print(e)



    # table_5 = onGuestsArrived(5)
    # onGuestsArrived(2)
    # onGuestsArrived(6)
    # onGuestsArrived(5)
    #
    # # no available tables left for 5
    # onGuestsArrived(5)
    # # there are still available table for 4
    # onGuestsArrived(4)
    # # a table with 5 guests is available now
    # japanika.release(table_5)
    # # now it is possible to reserve a table for 5 again
    # onGuestsArrived(5)