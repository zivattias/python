from lesson7.GadgetStore.orders.orders import *
class Customer:
    def __init__(self, name, address, phone, customer_id, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.customer_id = customer_id
        self.email = email

    def __str__(self):
        return f"<Customer Details>\n" \
               f"Customer name: {self.name}\n" \
               f"Customer address: {self.address}\n" \
               f"Customer phone: {self.phone}\n"

    def __repr__(self):
        return f"<REP: Customer {self.name}>"


class Product:
    def __init__(self, sku: str, category: str, brand: str, qty: int, price: float,
                 model: str = None,
                 warranty_months: int = None):
        if price <= 0:
            pass
            # Error
        self.sku = sku
        self.category = category
        self.brand = brand
        self.qty = qty
        self.price = price
        self.model = model
        self.warranty_months = warranty_months

    def update_stock(self, diff: int):
        if diff + self.qty < 0:
            print("You're trying to remove more items than you have.")
            return None
        self.qty += diff

    def update_price(self, new_price: int):
        if new_price <= 0:
            # Error
            return None
        self.price = new_price

    def __str__(self):
        return f"<Product>: Brand: {self.brand}, Model: {self.model}, SKU: {self.sku}, QTY: {self.qty}"

    def __repr__(self):
        return f"<Product>: SKU: {self.sku}, QTY: {self.qty}"

    def __eq__(self, other):
        return self.sku == other.sku


class Store:
    def __init__(self, store_name):
        self.store_name = store_name

        # id: Customer
        self.customers: {int: Customer} = dict()

        # sku to Product
        self.inventory: {str: Product} = dict()

        self.inventory_by_name: {str: Product} = dict()

        # Order num to order:
        self.orders: dict[int, Order] = {}

    # customers
    # inventory
    # order_product
    # orders_db
    # shipments

    def add_customer(self, name, address, phone, customer_id, email=None):
        new_customer = Customer(name, address, phone, customer_id, email)
        self.customers[customer_id] = new_customer

    def add_customer2(self, customer: Customer):
        self.customers[customer.customer_id] = Customer

    def display_customers(self):
        print(self.customers)

    def add_product_to_inventory(self, sku: str, category: str, brand: str, qty: int | float, price: float,
                                 model: str = None,
                                 warranty_months: int = None):
        print(f"Adding product {brand} {model}...")
        new_product = Product(sku, category, brand, qty, price, model, warranty_months)
        self.inventory[sku] = new_product
        self.inventory_by_name[brand + ' ' + model] = new_product

    def add_quantity_to_product(self, sku: str, qty: int | float):
        self.inventory[sku].update_stock(qty)

    def add_quantity_to_multiple_products(self, skus: list, quantities: list):
        for sku, qty in zip(skus, quantities):
            self.add_quantity_to_product(sku, qty)

    def get_products_by_brand(self, brand: str) -> list[Product]:
        ret_val = list()
        for product in self.inventory.values():
            # to check a variable inside a Class, you use: Class.variable; product.brand = Product.brand
            if product.brand == brand:
                ret_val.append(product)
        return ret_val

    def get_out_of_stock_products(self):
        pass

    def place_order(self, customer_id: int, order_id: int, sku: str,
                    qty: int, price_per_product: int) -> bool:
        # check if customer exists
        if customer_id not in self.customers:
            print("Can't place order for a non-existant customer")
            return False
        if qty > self.inventory[sku].qty:
            print("Unable to add order, not enough inventory.")
            return False
        if sku not in self.inventory:
            print("SKU not found.")
            return False
        # init Order:
        order = Order(customer_id, order_id)  # Order for Customer ID 100
        order.add_product(sku, qty, self.inventory[sku].price)  # Add SKU of Product to Order ID 1
        self.orders[order_id] = order
        # update inventory:
        self.inventory[sku].qty -= qty
        return True

    def display_orders(self):
        print(self.orders)
