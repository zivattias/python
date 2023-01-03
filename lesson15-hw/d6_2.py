# Implement a function that receives a csv file_path (str), and returns the following:
# List of column names
# Number of rows in the file
# Number of columns in the file
# Notes:
# you can assume that the csv file is correct and is not corrupted
# Consider using DictReader

import os
import csv


# Non-DictReader way:
def csv_data1(fp: str):
    if not os.path.exists(fp):
        raise Exception('Invalid file path')
    if os.path.splitext(fp)[1] != '.csv':
        raise Exception('Non-CSV given')
    with open(fp, 'r') as f:
        reader = csv.reader(f)
        col_list = next(reader)
        rows = len(f.readlines())
        return col_list, rows + 1, len(col_list)


# DictReader way:
def csv_data2(fp: str):
    if not os.path.exists(fp):
        raise Exception('Invalid file path')
    if os.path.splitext(fp)[1] != '.csv':
        raise Exception('Non-CSV file given')
    with open(fp, 'r') as f:
        file_dict = csv.DictReader(f)
        file_list = list(file_dict)
        return list(file_list[0].keys()), len(file_list) + 1, len(file_list[0].keys())


if __name__ == '__main__':
    print(csv_data1('./files/csv.csv'))
    print(csv_data2('./files/csv.csv'))
