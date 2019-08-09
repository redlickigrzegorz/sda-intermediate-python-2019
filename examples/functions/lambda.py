import typing
from collections import namedtuple

sum_ints = lambda a, b: a + b

Employee = namedtuple("Employee", ["name", "role", "salary"])

if __name__ == "__main__":
    print(sum_ints(2, 3))
    list1 = [2, 5, 4, 6, 9]
    print(sorted(list1))
    employee1 = Employee("Zenon", "Tester", 3500)
    employee2 = Employee("Jan", "Tester", 4000)
    employee3 = Employee("Stefan", "Developer", 5000)
    employees: typing.List[Employee] = [employee1, employee2, employee3]
    print(sorted(employees, key=lambda employee: employee.salary, reverse=True))
    print(sorted(employees, key=lambda employee: (employee.role, employee.name)))
    print("*************")
    print(min(employees, key=lambda employee: employee.salary))
    print(max(employees, key=lambda employee: employee.salary))
    print(max(employees, key=lambda e: e.salary))

    def salary_of_employee(e: Employee) -> int:
        return e.salary

    temp_function = salary_of_employee

    print(max(employees, key=temp_function))

    print("******************")

    list_1 = [1, 2, 3, 4, 5]
    """
    squared_list_1 = list(map(lambda number: number**2, list_1))
    print(squared_list_1)

    filtered_list_1 = list(filter(lambda number: not number%2, squared_list_1))
    print(filtered_list_1)
    """
    squared_list_1 = [number ** 2 for number in list_1]
    print(squared_list_1)

    filtered_list_1 = [number for number in squared_list_1 if not number % 2]
    print(filtered_list_1)
