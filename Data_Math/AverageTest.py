# load the data into working memory
from LoadingData.Data import Data
from Data_Math import  Average


def main():
    master_data = Data()
    master_data.load_data()
    data = master_data.get_data()

    # testing the average function
    average_list = Average.calculate_store_averages(data)


if __name__ == '__main__':
    main()
