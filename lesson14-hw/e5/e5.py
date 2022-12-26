# E5 v2

from exceptions import *
import time
import csv
import os
import concurrent.futures


class FileProcessor:
    def __init__(self, file: str, path: str, delimiter: str = ','):
        if not os.path.exists(path):
            raise InvalidDirectory(path)
        self._path = path

        if not os.path.isfile(file) or os.path.splitext(file)[1] != '.csv':
            raise InvalidFile(file)
        self._file = file

        with open(self._file, 'r') as f:
            reader = csv.reader(f)
            self._data = list(reader)

        self._delimiter = delimiter

    @property
    def path(self) -> str:
        return self._path

    @property
    def delimiter(self) -> str:
        return self._delimiter

    @path.setter
    def path(self, val):
        self._path = val

    @delimiter.setter
    def delimiter(self, val):
        self._delimiter = val

    def process_year(self, year):
        data = self._data
        year_specific_data = [entry for entry in data[1::] if entry[0].split('-')[2] == year]
        # Legend: Date, Low, Open, Volume, High, Close, Adjusted Close
        average_low = sum(float(entry[1]) for entry in year_specific_data) / len(year_specific_data[1::])
        average_open = sum(float(entry[2]) for entry in year_specific_data) / len(year_specific_data[1::])
        average_volume = sum(float(entry[3]) for entry in year_specific_data) / len(year_specific_data[1::])
        average_high = sum(float(entry[4]) for entry in year_specific_data) / len(year_specific_data[1::])
        average_close = sum(float(entry[5]) for entry in year_specific_data) / len(year_specific_data[1::])
        average_adj = sum(float(entry[6]) for entry in year_specific_data) / len(year_specific_data[1::])

        full_path = os.path.join(self.path, f"AAPL_{year}.csv")
        with open(full_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data[0])
            writer.writerows(year_specific_data)
            writer.writerow([year, average_low, average_open, average_volume, average_high,
                             average_close, average_adj])

    def main(self):
        data = self._data
        years = sorted(set(entry[0].split('-')[2] for entry in data[1::]))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            tasks = [executor.submit(self.process_year, year) for year in years]

        done, undone = concurrent.futures.wait(tasks, return_when=concurrent.futures.ALL_COMPLETED)
        return done, undone


if __name__ == '__main__':
    start = time.perf_counter()
    file = FileProcessor('aapl_data.csv', 'processed_files')
    tasks = file.main()
    end = time.perf_counter()
    print(f"Done: {len(tasks[0])}, undone: {len(tasks[1])} | Elapsed time: {(end - start):2f} second(s)")
