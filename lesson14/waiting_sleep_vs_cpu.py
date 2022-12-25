import time


def wait_using_sleep(sec):
    print("Counting down")
    start = time.time()
    time.sleep(sec)
    print(f"{time.time() - start}")
    print(f"{sec} seconds is over")


# Busy wait - refrain from using this way, since it overloads the CPU
def wait_wasting_cpu(sec):
    print("Counting down")
    start = time.time()
    while time.time() - start < 5:
        continue
    print(f"{time.time() - start}")
    print(f"{sec} seconds is over")


if __name__ == '__main__':
    wait_using_sleep(5)
    wait_wasting_cpu(5)
