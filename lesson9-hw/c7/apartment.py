class Apartment:
    def __init__(self, address: str, parking_type: str, rooms_num: float, size: float, floor: int, has_balcony: bool,
                 is_penthouse: bool, is_villa: bool):
        self._address = address
        self._parking_type = parking_type
        self._rooms_num = rooms_num
        self._size = size
        self._floor = floor
        self._has_balcony = has_balcony
        self._is_penthouse = is_penthouse
        self._is_villa = is_villa
        self._deal_state = False


class ForSale(Apartment):
    def __init__(self, address: str, parking_type: str, rooms_num: float, size: float, floor: int, has_balcony: bool,
                 is_penthouse: bool, is_villa: bool, sale_price: float, monthly_municipal_tax: float):
        super().__init__(address, parking_type, rooms_num, size, floor, has_balcony, is_penthouse, is_villa)
        self._sale_price = sale_price
        self._deal_state = True
        self._monthly_municipal_tax = monthly_municipal_tax

    def get_annual_municipal_tax(self) -> float:
        annual_municipal_tax = self._monthly_municipal_tax * 12
        return annual_municipal_tax

    def get_sale_price(self) -> float:
        return self._sale_price

    def is_for_sale(self) -> bool:
        return True if self._deal_state is True else False


class ForRent(Apartment):

    def __init__(self, address: str, parking_type: str, rooms_num: float, size: float, floor: int, has_balcony: bool,
                 is_penthouse: bool, is_villa: bool, rent_price: float):
        super().__init__(address, parking_type, rooms_num, size, floor, has_balcony, is_penthouse, is_villa)
        self._rent_price = rent_price
        self._deal_state = True

    def get_annual_rent_price(self) -> float:
        annual_rent_price = self._rent_price * 12
        return annual_rent_price

    def get_rent_price(self) -> float:
        return self._rent_price

    def is_for_rent(self) -> bool:
        return True if self._deal_state is True else False


def get_agency_fee(apartment: Apartment | ForRent | ForSale) -> float | str:
    if isinstance(apartment, ForSale):
        agency_fee = 0.02 * ForSale.get_sale_price(apartment)
        return agency_fee
    elif isinstance(apartment, ForRent):
        agency_fee = ForRent.get_rent_price(apartment)
        return agency_fee
    else:
        error = f"Apartment {apartment._address} is neither for sale or rent."
        return error


def set_deal_status(apartment: ForSale | ForRent) -> bool:
    apartment._deal_state = False
    return True


def close_deal(apartment: ForSale | ForRent) -> bool:
    if not isinstance(apartment, ForSale) or not isinstance(apartment, ForRent):
        return False
    return set_deal_status(apartment)
