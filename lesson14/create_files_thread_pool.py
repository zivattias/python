import concurrent
import datetime
import os
from concurrent.futures import ThreadPoolExecutor, wait


def create_files(base_prefix: str, num: int):
    if not os.path.exists(base_prefix):
        os.makedirs(base_prefix)

    executor = ThreadPoolExecutor(max_workers=16)
    futures = []

    for i in range(1, num + 1):
        file_path = os.path.join(base_prefix, f"factorial_{i}.txt")

        # print(f"Started calculating for {i}")
        lines = []
        for j in range(100):
            lines.append(f"{i} in power {j} is: {i ** j}")
        # print(f"Finished calculating for {i}")

        future = executor.submit(create_single_file, file_path, i, lines)  # does not block
        futures.append(future)

    done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")

    # executor.shutdown(wait=True) # or with context manager


def create_single_file(file_path, i, lines):
    # print(f"Started writing for {i}")
    with open(file_path, 'w') as f:
        f.writelines(lines * 200)
    # print(f"Finished writing for {i}")


if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    create_files("/Users/ziv.attias/temp", 700)
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end - start).total_seconds()}s")
