# Write a function that receives a directory path, searches there for csv files,
# and if csv files exist - return the following data for each: filename, amount of columns, amount of rows.
# You can assume that all the csv files are in the correct format.
# Make sure you handle properly a case in which the provided path does not exist.
# In addition, you should take into account that there can be inner folders with files and you should find them all.
# Test your code with this folder.
# Hint: check out os.walk function to iterate directory.

path = '/Users/ziv.attias/PycharmProjects/python-course/lesson9-hw/files_ex'

import os

def csv_checker(dir_path: str):
    if os.path.exists(path) is False:
        print('Bad path.')
        return False
    for (root, dirs, files) in os.walk(dir_path, topdown=True):
        for file in files:
            if file.endswith('.csv'):
                with open(f"{root}/{file}", 'r') as f:
                    print(f"Filename: {file}")
                    cols = len(f.readline().split(','))
                    print(f"Columns: {cols}")
                    rows = 1
                    while f.readline():
                        rows += 1
                    print(f"Rows: {rows}\n")

if __name__ == '__main__':
    csv_checker(path)