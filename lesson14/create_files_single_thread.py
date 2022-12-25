# motivating task: given base filename and number n,
# create n files and write some text inside them
import datetime
import os.path
from math import factorial


def create_files(base_prefix: str, num: int):
    if not os.path.exists(base_prefix):
        os.makedirs(base_prefix)

    for i in range(1, num+1):
        # print(f"Started calculating for {i}")
        lines = []
        for j in range(100):
            lines.append(f"{i} in power {j} is: {i ** j}")
        # print(f"Finished calculating for {i}")

        file_path = os.path.join(base_prefix, f"factorial_{i}.txt")

        # print(f"Started writing for {i}")
        with open(file_path, 'w') as f:
            f.writelines(lines*200)
        # print(f"Finished writing for {i}")


if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    create_files("/Users/ziv.attias/temp", 30)
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end-start).total_seconds()}s")