from lesson7.GadgetStore.store.gadget_store import Store

if __name__ == '__main__':
    my_store = Store('Gadgets Store')
    my_store.add_customer('Ziv Attias', 'Tel Aviv-Yafo', '052-8039540', 100)
    my_store.add_customer('Noa Gilboa', 'Tel Aviv-Yafo', '054-4444444', 101)
    # sample_customer = Customer('Israel Israeli', 'TLV', '052-2222222', 1002, 'ilil@gmail.com')
    # my_store.add_customer2(sample_customer)

    # print(my_store.customers["Ziv Attias"])
    # print(my_store.customers["Noa Gilboa"])
    # print(my_store.customers["Israel Israeli"])

    my_store.display_customers()

    my_store.add_product_to_inventory("A1234", "Computers", "Apple", 5, 1000, "MacBook Pro", 12)
    print(my_store.inventory["A1234"])
    my_store.place_order(100, 456, "A1234", 2, 1000)
    print(my_store.inventory["A1234"])
    # my_store.place_order(100, order1)

    my_store.display_orders()

