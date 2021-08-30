class Store:
    def __init__(self, id, type, size):
        self.__id = id
        self.__type = type
        self.__size = size
        self.__departments = {}
        self.__external_factors = {}

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_size(self):
        return self.__size

    def get_departments(self):
        return self.__departments

    def set_id(self, id):
        self.__id = id

    def set_type(self, type):
        self.__type = type

    def set_size(self, size):
        self.__size = size

    def set_departments(self, department_objects):
        self.__departments = department_objects

    def add_department(self, single_department_object):
        self.__departments[single_department_object.get_id()] = single_department_object

    def add_external_factor(self, external_factor):
        self.__external_factors[external_factor.get_date()] = external_factor

    def get_external_factors(self):
        return self.__external_factors

    # print all store weekly transactions
    def print_all_transactions(self):
        print("Store ID: ", self.__id, "\tType: ", self.__type, "\tSize: ", self.__size)
    #      iterate over departments
        for department in self.__departments.values():
            print("\tDepartment ID: ", department.get_id())
            for weekly_sale in department.get_weekly_sales().values():
                print("\t\tDate: ", weekly_sale.get_date(), "\tSale Amount: ", weekly_sale.get_amount(),
                      "\tIs Holiday: ", weekly_sale.get_is_holiday())
    #       iterate over department transactions

#  get life time store earnings
    def calculate_lifetime_earnings(self):
        total = 0
        for item in self.__departments.values():
            total += item.calculate_lifetime_sales()
        return total

    def calculate_average_weekly_sales(self):
        total_sales = 0
        total_records = 0
        for department in self.__departments.values():
            for transaction in department.get_weekly_sales().values():
                total_sales += transaction.get_amount()
                total_records += 1
        return total_sales / total_records

    def to_string(self):
        return "Store ID: {0:10} Type: {1:10} Size: {2:,}".format(str(self.__id), self.__type, self.__size)

#     print list of store external factors

