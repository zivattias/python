# The last line of each file should contain a row with averages of the data for this year.


import csv
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


class AAPLFile:
    def __init__(self, path: str, delimiter: str = ','):
        self._path = path
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

    def valid_dir(self):
        directory = 'files'
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def get_years_list(self):   # CPU bound operation
        years = []
        with open(self.path, 'r') as f:
            reader = csv.DictReader(f, delimiter=self.delimiter)
            for line in reader:
                year = line['Date'].split('-')[2]
                if year not in years:
                    years.append(year)
        return years

    def write_files(self):  # IO bound operation
        # check for 'files' directory existence
        self.valid_dir()

        # get CSV lines from original file
        with open(self.path, 'r') as f_r:
            reader = csv.DictReader(f_r, delimiter=self.delimiter)
            fieldnames = reader.fieldnames

            for year in self.get_years_list():
                with open(f'files/AAPL_{year}.csv', 'w') as f_w:
                    writer = csv.DictWriter(f_w, fieldnames=fieldnames)
                    writer.writeheader()

            for line in reader:
                year = line['Date'].split('-')[2]
                with open(f'files/AAPL_{year}.csv', 'a') as f_w:
                    writer = csv.DictWriter(f_w, fieldnames=fieldnames)
                    writer.writerow(line)

    def get_averages(self):
        directory = self.valid_dir()

        averages = dict()

        for file in os.listdir(directory):
            print(file)



if __name__ == '__main__':
    file = AAPLFile('AAPL.csv')
    file.get_averages()
