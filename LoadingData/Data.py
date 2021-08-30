from Classes import Store, ExternalFactors, WeeklySaleRecord, Department


class Data:
    __store_file_location = "../DataSets/stores data-set.csv"
    __sales_data_file = "../DataSets/sales data-set.csv"
    __external_factors_data_file = "../DataSets/Features data set.csv"
    __data_dictionary = {}


    def __basic_read_file(self, data_file):
        file = open(data_file, "r")
        my_data = list()
        for line in file:
            line = line.strip("\n")
            my_data.append(line)
        file.close()
        return my_data

    def __load_store_data(self):
        store_list = self.__basic_read_file(self.__store_file_location)
        for line in store_list[1:]:
            split = line.split(",")
            temp_store = Store(int(split[0]), split[1], int(split[2]))
            self.__data_dictionary[temp_store.get_id()] = temp_store

    def __load_external_data(self):
        external_factors_line_list = self.__basic_read_file(self.__external_factors_data_file)
        for line in external_factors_line_list[1:]:
            split = line.split(",")
            # print(len(split))
            # print(f'1{split[1]}\n2{split[2]}\n3{split[3]}\n4{split[4]}\n5{split[5]}\n6{split[6]}\n7{split[7]}\n8{split[8]}\n9{split[9]}\n10{split[10]}')
            temp_external_factors = ExternalFactors (split [1], split [2], split [3], split [4], split [5], split [6], split [7],
                                    split [8], split [9], split [10], split [11])
            self.__data_dictionary[int(split[0])].add_external_factor(temp_external_factors)

    def __load_weekly_sales(self):
        weekly_sale_line_list = self.__basic_read_file(self.__sales_data_file)
        for line in weekly_sale_line_list[1:]:
            split = line.split(",")
            temp_weekly_sale = WeeklySaleRecord(split[2], float(split[3]), split[4])
            store = self.__data_dictionary.get(int(split[0]))
            if int(split[1]) in store.get_departments():
                store.get_departments().get(int(split[1])).add_weekly_sale(temp_weekly_sale)
            else:
                temp_department = Department(int(split[1]))
                temp_department.add_weekly_sale(temp_weekly_sale)
                store.add_department(temp_department)

    def get_data(self):
        return self.__data_dictionary

    def load_data(self):
        print("Loading Data...")
        self.__load_store_data()
        print("Store data: Done")
        self.__load_external_data()
        print("External data: Done")
        self.__load_weekly_sales()
        print("Sales data: Done")
