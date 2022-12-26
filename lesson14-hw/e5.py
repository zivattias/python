# The last line of each file should contain a row with averages of the data for this year.


import csv
import os
import concurrent.futures


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

    def get_years_list(self):  # CPU bound operation
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

                    print(f'Finished headers for {f_w.name}')

            for i, line in enumerate(reader):
                if i != 0 and line['Date'].split('-')[2] != year:
                    print(f'Finished lines for {f_w.name}')
                year = line['Date'].split('-')[2]
                with open(f'files/AAPL_{year}.csv', 'a') as f_w:
                    writer = csv.DictWriter(f_w, fieldnames=fieldnames)
                    writer.writerow(line)


    def calc_averages(self):  # CPU bound operation
        directory = self.valid_dir()

        low_sum = open_sum = vol_sum = high_sum = close_sum = adj_sum = 0

        for file in os.listdir(directory):
            year = file.split('_')[1].split('.')[0]
            full_file_path = os.path.join(directory, file)

            with open(full_file_path, 'r') as f:
                reader = csv.DictReader(f, delimiter=self.delimiter)
                fieldnames = reader.fieldnames

                lines_counter = 0
                for line in reader:
                    low_sum += float(line['Low'])
                    open_sum += float(line['Open'])
                    vol_sum += float(line['Volume'])
                    high_sum += float(line['High'])
                    close_sum += float(line['Close'])
                    adj_sum += float(line['Adjusted Close'])
                    lines_counter += 1

                row_dict = {'Date': year,
                            'Low': low_sum / lines_counter,
                            'Open': open_sum / lines_counter,
                            'Volume': vol_sum / lines_counter,
                            'High': high_sum / lines_counter,
                            'Close': close_sum / lines_counter,
                            'Adjusted Close': adj_sum / lines_counter}

                print(f'Calculated averages for file: {full_file_path}')

            self._write_averages(full_file_path, fieldnames, row_dict)

    @staticmethod
    def _write_averages(full_file_path, fieldnames, row_dict):   # IO bound operation
        with open(full_file_path, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(row_dict)

        print(f'Wrote averages for file {full_file_path}')


if __name__ == '__main__':
    og = AAPLFile('aapl_data.csv')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        t1 = executor.submit(og.write_files)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        p1 = executor.submit(og.calc_averages)

    # og.write_files()
    # og.calc_averages()