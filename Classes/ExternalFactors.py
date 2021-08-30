class ExternalFactors:
    __date = None
    __temperature = None
    __fuel_price = None
    __mark_down_one = None
    __mark_down_two = None
    __mark_down_three = None
    __mark_down_four = None
    __consumer_price_index = None
    __unemployment = None
    __is_holiday = None

    def __init__(self, date, temp, fuel, markdown_one, markdown_two, markdown_three, markdown_four, markdown_five, cpi,
                 unemployment, is_holiday):
        self.__date = date
        self.__temperature = temp
        self.__fuel_price = fuel
        self.__mark_down_one = markdown_one
        self.__mark_down_two = markdown_two
        self.__mark_down_three = markdown_three
        self.__mark_down_four = markdown_four
        self.__mark_down_five = markdown_five
        self.__consumer_price_index = cpi
        self.__unemployment = unemployment
        self.__is_holiday = is_holiday

#     get and set methods
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temp):
        self.__temperature = temp

    # to string data
    def to_string(self):
        return "Date: {}\n" \
               "Temperature: {}\n" \
               "Fuel Price: ${}\n" \
               "Mark Down One: ${}\n" \
               "Mark Down Two: ${}\n" \
               "Mark Down Three: ${}\n" \
               "Mark Down Four: ${}\n" \
               "Consumer Price Index: {}\n" \
               "Unemployment: {}\n" \
               "Holiday: {}".format(self.__date, self.__temperature, self.__fuel_price, self.__mark_down_one,
                                    self.__mark_down_two, self.__mark_down_three, self.__mark_down_four,
                                    self.__consumer_price_index, self.__unemployment, self.__is_holiday)
