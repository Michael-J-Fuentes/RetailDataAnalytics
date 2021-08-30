from Classes import Store, ExternalFactors, WeeklySaleRecord, Department
from LoadingData import ReadFilesSimple

store_data_dictionary = {}


#  transform data from list to objects for store data
def load_stores_into_dictionary(list_data):
    for line in list_data[1:]:
        # split the line based on comma seperator
        split = line.split(",")
        temp = Store(int(split[0]), split[1], int(split[2]))
        #  add the objects to the main hash map
        store_data_dictionary[temp.get_id()] = temp


def prof_that_store_data_is_stored_for_testing():
    load_stores_into_dictionary(ReadFilesSimple.read_store_data())
    for key in store_data_dictionary.keys():
        print(store_data_dictionary[key].to_string())


# prof_that_store_data_is_stored_for_testing()


# load external factors into master data, matching store id to external data
def load_external_factors_into_dictionary(list_data):
    for line in list_data[1:]:
        split = line.split(",")
        temp = ExternalFactors(split[1], split[2], split[3], split[4], split[5], split[6], split[7],
                               split[8], split[9], split[10], split[11])
        store_data_dictionary[int(split[0])].add_external_factor(temp)


def prof_that_external_data_is_stored_for_testing():
    prof_that_store_data_is_stored_for_testing()
    load_external_factors_into_dictionary(ReadFilesSimple.read_features_data())
    for store in store_data_dictionary.keys():
        print(store_data_dictionary[store].get_id())
        for external_factor in store_data_dictionary[store].get_external_factors().values():
            print(store, "\n", external_factor.to_string())
            print()


# prof_that_external_data_is_stored_for_testing()


# load department and sales data into main file
def load_sales_data_into_dictionary(list_data):
    for line in list_data[1:]:
        split = line.split(',')
        temp_weekly_sale = WeeklySaleRecord(split[2], split[3], split[4])
        # check if the department already exist in the master directory
        store = store_data_dictionary.get(int(split[0]))
        if int(split[1]) in store.get_departments():
        #     get the weekly sale and add it the existing object
            store.get_departments().get(int(split[1])).add_weekly_sale(temp_weekly_sale)
        else:
            temp_department = Department(int(split[1]))
            temp_department.add_weekly_sale(temp_weekly_sale)
            store.add_department (temp_department)
        # get store from id


def prof_that_sale_data_is_stored_for_testing():
    load_sales_data_into_dictionary(ReadFilesSimple.read_sales_data())
    for store in store_data_dictionary.values():
        print(store.to_string())
        # print(len(store.get_departments()))
        for dep in store.get_departments().values():
            print(len(dep.get_weekly_sales().values()))
        # for department in store.get_departments().values():
            # print(store.get_id())
            # print(department.get_department_records())

# Loading all data in for testing
load_stores_into_dictionary(ReadFilesSimple.read_store_data())
load_external_factors_into_dictionary(ReadFilesSimple.read_features_data())
prof_that_sale_data_is_stored_for_testing()