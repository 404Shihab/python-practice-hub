class Employee:
    company = "ABC"
    def show(self):
        print(f"The name of employee is {self.employee} and the salary is {self.salary}")


class Programmer(Employee):
    company = "abc it"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good at {self.language} Language")


parent = Employee()
child = Programmer()

print(parent.company, child.company)