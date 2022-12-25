import threading


def a_lot_of_calcs(num: int):
    print(f"Started {a_lot_of_calcs.__name__} with {num}")
    s = 0
    for i in range(10_000):
        s += num ** i
    print(f"Finished {a_lot_of_calcs.__name__} with {s}\n")


if __name__ == '__main__':
    print('Program start')

    num1 = int(input('Enter your num: '))
    t = threading.Thread(target=a_lot_of_calcs, args=[num1])
    t.start()  # non-blocking action

    num2 = int(input('Enter your num: '))
    t1 = threading.Thread(target=a_lot_of_calcs, args=[num2])
    t1.start()

    t.join()  # blocking action: merging 't' thread to Main Thread
    t1.join()  # blocking action: merging 't1' thread to Main Thread
    print('Program finish')
