from unittest import TestCase
from table_system import Table, TableReservationSystem
from table_system_exceptions import *


class TableTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.table_sys = TableReservationSystem([4, 4, 2, 2, 10], 'EduLabs')

    def test_reserve(self):
        self.table_sys.reserve(4, 0)
        self.assertFalse(self.table_sys.tables[0].is_available())
        self.assertEqual(self.table_sys.tables[0].occupied_seats, 4)

        self.table_sys.reserve(3, 1)
        self.assertFalse(self.table_sys.tables[1].is_available())
        self.assertEqual(self.table_sys.tables[1].occupied_seats, 3)

        with self.assertRaises(TableAlreadyOccupied):
            self.table_sys.reserve(1, 0)
            self.table_sys.reserve(5, 1)

        with self.assertRaises(InsufficientSeatsInTable):
            self.table_sys.reserve(3, 2)
            self.table_sys.reserve(3, 3)

        with self.assertRaises(TableNotFound):
            self.table_sys.reserve(1, 7)

    def test_release(self):
        self.table_sys.reserve(1, 1)
        self.table_sys.release(1)
        self.assertEqual(self.table_sys.tables[1].occupied_seats, 0)

        with self.assertRaises(TableAlreadyAvailable):
            self.table_sys.release(4)

        with self.assertRaises(TableNotFound):
            self.table_sys.release(5)
