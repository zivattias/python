from datetime import datetime, timedelta

from table import Table


class Floor:
    # Tables counter:
    total_tables = 0

    # INITIALIZE FLOOR:
    def __init__(self):
        self.tables_dict: dict[int, Table] = {}

    # Create a table, add to tables_dict and increment tables counter:
    def create_table(self, table_id: int, capacity: int):
        if table_id in self.tables_dict:
            print(f"Table ID {table_id} already exists.")
            return False
        table = Table(table_id, capacity)
        self.tables_dict[table_id] = table
        self.total_tables += 1

    # Display certain table details:
    def table_details(self, table_id):
        if table_id not in self.tables_dict:
            print('Wrong table number.')
            return False
        print(self.tables_dict[table_id])

    def display_all_tables(self):
        for table in self.tables_dict.values():
            print(table)

    # Get ALL available tables for a given guests num:
    def is_available(self, guests: int) -> list[list[int]] | bool:
        available_tables = list()
        for table in self.tables_dict.values():
            if table.capacity >= guests and table.is_available is True:
                available_tables.append([table.table_id, table.capacity])
        if len(available_tables) == 0:
            print('No available tables.')
            return False
        return sorted(available_tables, key=lambda t: t[1])

    # Reserve a table for guests num:
    def reserve(self, table_id: int, guests: int):
        if table_id not in self.tables_dict:
            print(f"Table ID {table_id} not found.")
            return False
        if guests > self.tables_dict[table_id].capacity:
            print(f"Table {table_id} doesn't have enough seats to accommodate {guests} guests.")
            return False
        self.tables_dict[table_id].reserve()
        self.tables_dict[table_id].occupied_seats = guests

    # Release a table by table ID:
    def release(self, table_id: int):
        if table_id not in self.tables_dict:
            print(f"Table with ID {table_id} not found.")
            return False
        if self.tables_dict[table_id].is_available is True:
            print(f"Table {table_id} is already free.")
            return False
        self.tables_dict[table_id].release()

    # Get time left until for given table ID availability:
    def time_left_for_table(self, table_id: int) -> timedelta | bool:
        if table_id not in self.tables_dict:
            print(f"Table with ID {table_id} not found.")
            return False
        if self.tables_dict[table_id].is_available is True:
            print(f"Table {table_id} is available. No time to display.")
            return False
        time_left = self.tables_dict[table_id].reservation_limit - datetime.now()
        return time_left

    # Get available tables for num of guests, sorted by soonest availability AND capacity:
    def get_soonest_available_tables(self, guests: int) -> list | bool:
        soonest_available_tables = list()
        for table in self.tables_dict.values():
            if table.capacity >= guests:
                time_left = self.time_left_for_table(table.table_id)
                soonest_available_tables.append([table.table_id, str(time_left), table.capacity])
        return sorted(soonest_available_tables, key=lambda t: (t[1], t[2]))

    # Get a table with less than X minutes left for availability:
    def get_table_with_x_minutes_left(self, min_left: int | float, guests: int):
        tables = list()
        for table in self.tables_dict.values():
            duration = self.time_left_for_table(table.table_id)
            time_in_minutes = (duration.total_seconds() % 3600) // 60 + (duration.total_seconds() // 3600 * 60)
            if table.capacity >= guests and time_in_minutes <= min_left:
                tables.append([table.table_id, time_in_minutes])
        return tables
