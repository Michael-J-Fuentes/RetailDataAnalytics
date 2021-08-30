# output a list of store averages
def calculate_store_averages(store_dictionary):
    avg_list = list()
    for store in store_dictionary.values():
        avg_list.append(store.calculate_average_weekly_sales())
    return avg_list


# print the averages of each store
def print_store_average(store_dictionary):
    avg_list = calculate_store_averages(store_dictionary)
    store_ids = list(store_dictionary.keys())
    for i in range(len(avg_list)):
        print(f'Store {store_ids[i]} Average: ${avg_list[i]:,.2f}')