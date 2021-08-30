# create a temp store object
from Classes.Store import Store
from Classes.WeeklySaleRecord import WeeklySaleRecord
from Classes.Department import Department
from Classes.ExternalFactors import ExternalFactors


def main():
    temp_exernal_factors = ("08-02-2021", 42.31, 2.572, None, None, None, None, 211.0964, 8.106, False)
    temp_store = Store(1, "A", 10000, temp_exernal_factors)

#     Create weekly sale
    temp_weekly_sale = WeeklySaleRecord("08-02-2021", 24924.5, False)
    temp_two_weekly_sale = WeeklySaleRecord("09-02-2021", 53231, True)
    temp_three_weekly_sale = WeeklySaleRecord("10-02-2021", 32413, False)

#     Create a temp department
    temp_department = Department(1)
    temp_two_department = Department(2)

#     add the weekly sale to department
    temp_department.add_weekly_sale(temp_weekly_sale)
    temp_department.add_weekly_sale(temp_two_weekly_sale)
    temp_two_department.add_weekly_sale(temp_three_weekly_sale)
#     add department to store
    temp_store.add_department(temp_department)
    temp_store.add_department(temp_two_department)

#     print department stores weekly sales record
    print(temp_department.get_department_records())
    print(temp_two_department.get_department_records())

#     print the store values
#     temp_store.print_all_transactions()

# print the department total transaction amount
    print("Department Lifetime Earnings: ${:,.2f}".format(temp_department.calculate_lifetime_sales()))

# print life time store earnings
    print("Store Lifetime Earnings: ${:,.2f}".format(temp_store.calculate_lifetime_earnings()))


if __name__ == "__main__":
    main()

