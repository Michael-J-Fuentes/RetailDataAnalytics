class AverageRecord:
    def __init__(self, store, average_record):
        self.__store = store
        self.__average_record = average_record

    def get_store(self):
        return self.__store

    def set_store(self, store):
        pass

    def get_average_record(self):
        return self.__average_record

    def set_average_record(self, average_record):
        self.__average_record = average_record
