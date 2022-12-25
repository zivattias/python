import datetime
import os
import threading
from math import factorial

# with open('AAPL.csv', 'r') as f:
#     csv_text = f.read()


def create_files(base_prefix: str, num: int):
    if not os.path.exists(base_prefix):
        os.makedirs(base_prefix)

    threads = []
    for i in range(1, num+1):
        file_path = os.path.join(base_prefix, f"factorial_{i}.txt")

        # print(f"Started calculating for {i}")
        lines = []
        for j in range(100):
            lines.append(f"{i} in power {j} is: {i ** j}")
        # print(f"Finished calculating for {i}")

        t = threading.Thread(target=create_single_file, args=(file_path, i, lines)) # not blocks
        threads.append(t)
        t.start() # not blocks

    # why not this?
    # for t in threads:
    #     t.start()

    for t in threads:
        t.join() # blocks


def create_single_file(file_path, i, lines):
    # print(f"Started writing for {i}")
    with open(file_path, 'w') as f:
        f.writelines(lines*200)
    # print(f"Finished writing for {i}")


if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    create_files("/Users/ziv.attias/temp", 36) # 36 | 300 | 700 - no improvemetn
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end-start).total_seconds()}s")