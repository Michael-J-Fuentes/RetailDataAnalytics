class Department:
    __id = None
    # __weekly_sales = None
    # Key Date : Values Sale record

    def __init__(self, id):
        self.__id = id
        self.__weekly_sales = {}

    def get_id(self):
        return self.__id

    def get_weekly_sales(self):
        return self.__weekly_sales

    def set_id(self, id):
        self.__id = id

#     adding things to dictionary
    def add_weekly_sale(self, weekly_sale):
        print("Adding date: " + weekly_sale.get_date())
        self.__weekly_sales[weekly_sale.get_date()] = weekly_sale

#     removing a item from dictionary
    def remove_weekly_sale(self, weekly_sale):
        if self.__weekly_sales.__contains__(weekly_sale):
            self.__weekly_sales.__delitem__(weekly_sale)

    def get_department_records(self):
        # my_string = "Department ID: " + str(self.__id) + "\n"
        my_string = "Department ID: {:3}\n".format(str(self.__id))
        for item in self.__weekly_sales.values():
            my_string += item.get_weekly_sale() + "\n"
        return my_string

#     get total number of sales, lifetime
    def calculate_lifetime_sales(self):
        total = 0
        for item in self.__weekly_sales.values():
            total += item.get_amount()
        return total

    def calculate_average_weekly_sales(self):
        return self.calculate_lifetime_sales() / len(self.__weekly_sales.keys())

    def to_string(self):
        return "ID: " + self.__id + "\n" + self.get_department_records()