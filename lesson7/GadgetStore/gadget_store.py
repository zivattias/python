class Customer:
    def __init__(self, name, address, phone, email=None):
        self.name = name
        self.address = address
        self.phone = phone
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
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        return self.sku == other.sku


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.customers: {str: Customer} = dict()
        self.inventory: {str: Product} = dict()
        self.inventory_by_name: {str: Product} = dict()

    # customers
    # inventory
    # order_product
    # orders_db
    # shipments

    def add_customer(self, name, address, phone, email=None):
        new_customer = Customer(name, address, phone, email)
        self.customers[name] = new_customer

    def add_product_to_inventory(self, sku: str, category: str, brand: str, qty: int | float, price: float,
                                 model: str = None,
                                 warranty_months: int = None):
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

    def add_order(self):
        pass
