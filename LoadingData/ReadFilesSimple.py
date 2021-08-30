# CONSTANTS
STORE_DATA_FILE = "../DataSets/stores data-set.csv"
SALES_DATA_FILE = "../DataSets/sales data-set.csv"
FEATURES_DATA_FILE = "../DataSets/Features data set.csv"

# Generic read file and load each line into a string
def basic_read_file(file_name):
    file = open(file_name, 'r')
    my_data = list()
    for line in file:
        line = line.strip("\n")
        my_data.append(line)
    file.close()
    return my_data


# Reading store data
def read_store_data():
    return basic_read_file(STORE_DATA_FILE)
# Reading features data set


def read_sales_data():
    return basic_read_file(SALES_DATA_FILE)


def read_features_data():
    return basic_read_file(FEATURES_DATA_FILE)

# Reading External Factors
