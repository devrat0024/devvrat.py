class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))

    employee = Employee(name, age, department, salary)
    employees.append(employee)
    print("Employee added successfully!")

def display_employees():
    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            employee.display_details()
            print("-" * 20)

while True:
    choice = input("Enter 'add' to add an employee, 'display' to view employees, or 'quit' to exit: ")

    if choice.lower() == 'add':
        add_employee()
    elif choice.lower() == 'display':
        display_employees()
    elif choice.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")