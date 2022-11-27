class Converter:

    def __init__(self):
        self.rates = {}
        self.USD_rates = {}

    def display_all_rates_to_USD(self) -> dict:
        return self.rates

    def display_all_rates_from_USD(self) -> dict:
        for k, v in self.rates.items():
            self.USD_rates[k] = 1 / v
        return self.USD_rates

    def add_rate(self, new_currency: str, value: int | float):
        if new_currency in self.rates.keys():
            print(f'The currency {new_currency} is already in the system.')
            return None
        self.rates[new_currency] = value
        print(f'The currency {new_currency} has been added.')

    def display_rate(self, currency):
        rate = self.rates.get(currency)
        return f"Rate for 1 USD: {rate} {currency}"

    def update_rate(self, currency: str, new_value: int):
        if currency not in self.rates.keys():
            print(f'The currency {currency} is not in the system, add it first.')
            return None
        self.rates[currency] = new_value

    def delete_rate(self, currency: str):
        if currency not in self.rates.keys():
            print(f'The currency {currency} is not in the system yet to delete it.')
            return None
        self.rates.pop(currency)
        return f'Rate for {currency} has been deleted.'

    def display_amount_currency(self, currency: str, amount_in_usd: int):
        if currency not in self.rates.keys():
            print(f'The currency {currency} is not in the system, add it first.')
            return None
        amount_converted = amount_in_usd / self.rates.get(currency)
        return f'{amount_in_usd} USD = {round(amount_converted, 4)} {currency}'

    def display_amount_USD(self, currency: str, amount_to_convert: int):
        if currency not in self.rates.keys():
            print(f'The currency {currency} is not in the system, add it first.')
            return None
        amount_in_usd = amount_to_convert / self.rates[currency]
        return f'{amount_to_convert} {currency} = {amount_in_usd} USD'
