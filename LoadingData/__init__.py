import os

import DataSets
from LoadingData import ReadFilesSimple


def main():
    file_name = "../DataSets/stores data-set.csv"
    my_data = ReadFilesSimple.basic_read_file(file_name)
    print(my_data)

    # my_data = ReadFilesSimple.basic_read_file(file_name)

if __name__ == '__main__':
    main()
