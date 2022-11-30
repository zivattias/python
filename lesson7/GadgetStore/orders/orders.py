from lesson7.GadgetStore.orders.shipments import Shipment
class Order:
    def __init__(self, customer_id: int, order_id: int):
        self.cart: dict = {}
        self.customer = customer_id
        self.order_id = order_id

    def add_product(self, sku: str, qty: int, price: int):
        self.cart[sku] = [qty, price]

    def get_total_price(self):
        total_sum = 0
        for product in self.cart.keys():
            total_sum += self.cart[product][0] * self.cart[product][1]
        print(total_sum)

    def print_cart(self):
        print(self.cart)

    def __repr__(self):
        return f'Order #{self.order_id} for Customer {self.customer}'

