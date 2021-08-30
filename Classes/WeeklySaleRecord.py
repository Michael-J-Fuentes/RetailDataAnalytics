# Record that holds how much is sold in a specific week
# each department will have several of this records, for 2 plus years
# the date will serve as the id, since a weekly record is unique
class WeeklySaleRecord:
    __date = None
    __amount = None
    __is_holiday = False

    def __init__(self, date, amount, is_holiday):
        self.__date = date
        self.__amount = amount
        self.__is_holiday = is_holiday

    def get_date(self):
        return self.__date

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount
        else:
            self.__amount = 0

    def set_date(self, date):
        self.__date = date

    def get_is_holiday(self):
        return self.__is_holiday

    def set_is_holiday(self, is_holiday):
        self.__is_holiday = is_holiday

    def get_weekly_sale(self):
        return "Date: {:20}Amount: {:20}Is Holiday: {:20}".format(self.__date, str(self.__amount), str(self.__is_holiday))
        # return "Date: " + self.__date + "\tAmount: " + str(self.__amount) + "\tIs Holiday: " + str(self.__is_holiday)

    def print_weekly_sale(self):
        print(self.get_weekly_sale())

