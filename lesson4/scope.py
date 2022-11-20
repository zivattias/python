prefix = 'Dr.'
months_in_year = 12


def append_doctor(name):
    global months_in_year
    months_in_year = 10
    print(months_in_year)
    ret_val = "Dr." + name
    return ret_val


append_doctor('ziv')
