from converter import *

if __name__ == '__main__':
    converter = Converter()

    print(converter.display_rate("YEN"))
    print(converter.display_amount_currency("YEN", 1))
    print(converter.display_amount_USD("YEN", 30000))
    print(converter.display_amount_USD("EUR", 134))
    print(converter.display_rate("EUR"))
    print(converter.delete_rate("YEN"))
    print(converter.display_all_rates_to_USD())
    print(converter.display_amount_USD("EUR", 3000))
    print(converter.display_all_rates_to_USD())
    converter.add_rate("YEN", 113.73)
    print(converter.display_amount_USD("YEN", 10000))
    converter.add_rate("CAD", 1.34)
    print(converter.display_all_rates_to_USD())
    print(converter.display_all_rates_from_USD())