class Shipment:
    # Static variable:
    STATUS = ('Processing', 'Shipped', 'Delivered')
    counter = 0  # - Total shipments recorded by __init__

    def __init__(self, address: str):
        self.address = address
        self.status = 0
        Shipment.counter += 1  # Will count how many times this function has been initialized =
        # How many times Shipment has been initialized

    def increment_status(self) -> bool:
        if self.status == len(Shipment.STATUS) - 1:
            print('Order has been already delivered')
            return False
        self.status += 1
        print(f'Order Status: {Shipment.STATUS[self.status]}')
        return True