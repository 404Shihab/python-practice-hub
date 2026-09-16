class Employee:
    def employeeInfo(self):
        print("This is employee information.")


class Programmer:
    def programmingInfo(self):
        print("This employee is good at programming.")


class Manager(Employee, Programmer):
    def managerInfo(self):
        print("This employee is a manager.")


person = Manager()

person.employeeInfo()
person.programmingInfo()
person.managerInfo()
