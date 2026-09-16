class Employee:

    company = "ABC"

    def __init__(self, employee, salary):
        self.employee = employee
        self.salary = salary

    def show(self):
        print(f"The name of employee is {self.employee} and the salary is {self.salary}")


class Programmer(Employee):
    company = "abc it"

    def __init__(self, employee, salary, name, language):
        super().__init__(employee, salary)
        self.name = name
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} Language")


parent = Employee("Shihab", 50000)

child = Programmer("Rahim", 60000, "Rahim", "Python")

print(parent.company, child.company)

parent.show()
child.show()
child.showLanguage()
