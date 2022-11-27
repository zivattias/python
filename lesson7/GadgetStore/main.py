from lesson7.GadgetStore.gadget_store import Store, Customer

if __name__ == '__main__':
    my_store = Store('Gadgets Store')
    my_store.add_customer('Ziv Attias', 'Tel Aviv-Yafo', '052-8039540')
    my_store.add_customer('Noa Gilboa', 'Tel Aviv-Yafo', '054-4444444')

    print(my_store.customers)

    print(my_store.customers["Ziv Attias"])
    print(my_store.customers["Noa Gilboa"])
