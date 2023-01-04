import csv
import json
import os
from abc import ABC, abstractmethod


class TextFile(ABC):
    def __init__(self, fp: str):
        if (not os.path.isfile(fp)) or os.path.splitext(fp)[-1][1:] != self._get_extension():
            raise Exception()
        self._fp = fp

    @abstractmethod
    def _get_content(self, fh):
        pass

    @abstractmethod
    def _get_extension(self):
        pass

    @staticmethod
    def get_combined_name(combined_fp: str) -> str:
        return combined_fp.split('/')[-1]

    def get_file_size(self):
        return os.path.getsize(self._fp)

    def get_file_path(self):
        return self._fp

    def return_content(self):
        with open(self._fp, 'r') as fh:
            content = self._get_content(fh)
        return content

    def get_combined_path(self, f2) -> str:
        f1_path = self.get_file_path()
        f2_path = f2.get_file_path()
        f1_name = os.path.splitext(f1_path)[0].split('/')[-1]
        f2_name = os.path.splitext(f2_path)[0].split('/')[-1]
        return f"{'/'.join(f1_path.split('/')[:-1])}/" \
               f"{f1_name}_{f2_name}.{self._get_extension()}"

    def __eq__(self, other) -> bool:
        return type(self) == type(other)

    def __add__(self, other):
        if self != other:
            raise TypeError("Objects of different types cannot be concatenated")

        if isinstance(self, JsonFile) or isinstance(other, JsonFile):
            raise TypeError('Concatenation not available for JSON files')

        combined_path = self.get_combined_path(other)
        if os.path.isfile(combined_path):
            raise Exception("File already exists, can't overwrite")

        self._concat(other)
        return True

    @abstractmethod
    def _concat(self, other):
        pass


class CsvFile(TextFile):

    def __init__(self, fp, delimiter=','):
        super().__init__(fp)
        self._delimiter = delimiter

    def get_delimiter(self) -> str:
        return self._delimiter

    def _get_extension(self) -> str:
        return 'csv'

    def _get_content(self, fh) -> list:
        ret_val = []
        for row in csv.DictReader(fh, delimiter=self.get_delimiter()):
            ret_val.append(row)
        return ret_val

    def get_rows_num(self) -> int:
        rows = 0
        with open(self.get_file_path(), 'r') as f:
            reader = csv.reader(f, delimiter=self.get_delimiter())
            for _ in reader:
                rows += 1
        return rows

    def get_columns_num(self) -> int:
        with open(self.get_file_path(), 'r') as f:
            reader = csv.reader(f, delimiter=self.get_delimiter())
            cols = len(next(reader))
        return cols

    def get_column(self, col_num: int) -> list:
        with open(self.get_file_path(), 'r') as f:
            reader = csv.reader(f, delimiter=self.get_delimiter())
            if col_num + 1 > len(next(reader)):
                raise IndexError('Column number is out of row range')
            f.seek(0)
            col_data = list()
            for line in reader:
                col_data.append(line[col_num])
        return col_data

    def get_cell(self, row_num, column_num) -> str:
        with open(self.get_file_path(), 'r') as f:
            reader = csv.reader(f, delimiter=self.get_delimiter())
            if row_num > self.get_rows_num() or column_num > self.get_columns_num():
                raise IndexError('Provided row/column out of range in file')
            for i, row in enumerate(reader):
                if i == row_num:
                    cell = row[column_num]
                    return cell

    def get_row(self, row_num: int) -> dict:
        with open(self.get_file_path(), 'r') as f:
            if row_num <= 0:
                raise ValueError("Row can't be zero (header) or negative")
            if row_num + 1 > self.get_rows_num():
                raise IndexError('Provided row out of range in file')
            csv_test = f.read(1024)
            f.seek(0)
            reader = csv.DictReader(f, delimiter=self.get_delimiter())
            for i, row in enumerate(reader):
                if i + 1 == row_num:
                    if csv.Sniffer().has_header(csv_test):
                        return row
                    ret_val = dict()
                    for key, value in enumerate(row):
                        ret_val[key + 1] = value
                    return ret_val

    def _concat(self, other):
        with open(self.get_file_path(), 'r') as file1, open(other.get_file_path(), 'r') as file2:
            reader1 = csv.DictReader(file1, delimiter=self.get_delimiter())
            reader2 = csv.DictReader(file2, delimiter=other.get_delimiter())
            headers1 = reader1.fieldnames
            headers2 = reader2.fieldnames
            if set(headers1) != set(headers2):
                raise ValueError('CSV files must contain equivalent headers (order irrelevant)')
            with open(self.get_combined_path(other), 'w') as new_f:
                writer = csv.DictWriter(new_f, fieldnames=reader1.fieldnames)
                writer.writeheader()
                for row in reader1:
                    writer.writerow(row)
                for row in reader2:
                    writer.writerow(row)
                return True


class TxtFile(TextFile):
    def _get_extension(self) -> str:
        return 'txt'

    def _get_content(self, fh) -> str:
        return fh.read()

    def _concat(self, other):
        merged_content = f"{self.return_content()} {other.return_content()}"
        with open(self.get_combined_path(other), 'w') as new_f:
            new_f.write(merged_content)

    def get_words_num(self) -> int:
        return len(self.return_content().split(' '))

    def get_avg_word_len(self) -> float:
        total_chars = len(''.join(self.return_content().split(' ')))
        total_words = self.get_words_num()
        return total_chars / total_words


class JsonFile(TextFile):
    def _get_extension(self) -> str:
        return 'json'

    def _get_content(self, fh):
        return json.load(fh)

    def _concat(self, other):
        pass

    def _load_json(self):
        with open(self.get_file_path(), 'r') as f:
            return json.load(f)

    def is_list(self) -> bool:
        return True if type(self._load_json()) is list else False

    def is_object(self) -> bool:
        return True if type(self._load_json()) is dict else False
