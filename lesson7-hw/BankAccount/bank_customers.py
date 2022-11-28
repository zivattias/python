class Person:
    def __init__(self, customer_id: int, name: str, address: str, phone: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        details = f'- PERSON #{self.customer_id} -\nNAME: {self.name}\nADDRESS: {self.address}\n' \
                  f'PHONE: {self.phone}\nEMAIL: {self.email}\n'
        return details

    def __repr__(self):
        return f"<PERSON: {self.customer_id}>"
