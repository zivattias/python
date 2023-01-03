# Implement a function that receives the following arguments:
# file_path (str, a path to a local file)
# start_line (int, line number to start reading from)
# end_line (int, the last line to read)
# The function should return a string that contains the lines that have been read.
# Note, you should check the correctness of the arguments
# (for example, whether there are enough lines in the file, or whether the file exists). Raise exceptions when needed.
import os


def read_lines(fp: str, start_line: int, end_line: int):
    if not os.path.exists(fp):
        raise Exception("Invalid path")
    with open(fp, 'r') as f:
        if len(f.readlines()) < end_line:
            raise Exception("End line exceeds max lines in file")
        f.seek(0)
        string = ''
        for line in f.readlines()[start_line - 1: end_line]:
            string += line.strip('\n') + ' '
    return string


if __name__ == '__main__':
    print(read_lines('./files/text.txt', 1, 5))
