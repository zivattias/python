from apartment import *

if __name__ == '__main__':
    apt = Apartment('30 Jerusalem Blvd', parking_type='street', rooms_num=4.5, size=80, floor=2,
                    has_balcony=True, is_villa=False, is_penthouse=False)

    apt2 = ForRent('31 Jerusalem Blvd', parking_type='underground', rooms_num=1, size=35, floor=1,
                   has_balcony=False, is_villa=False, is_penthouse=False, rent_price=3_500)

    apt3 = ForSale('32 Jerusalem Blvd', parking_type='private', rooms_num=6, size=100, floor=0,
                   has_balcony=True, is_villa=True, is_penthouse=False, sale_price=1_000_000,
                   monthly_municipal_tax=4_000)

    print(f"{apt2.get_rent_price():,} ILS")
    print(f"{apt3.get_sale_price():,} ILS")

    print(get_agency_fee(apt))
    print(f"{get_agency_fee(apt2):,} ILS")
    print(f"{get_agency_fee(apt3):,} ILS")

    print(apt3.is_for_sale())
    close_deal(apt3)
    print(apt3.is_for_sale())

    print(apt2.is_for_rent())
    close_deal(apt2)
    print(apt2.is_for_rent())

    print(close_deal(apt))

