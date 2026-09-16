class Employee:

    def employeeInfo(self):
        print("This is employee information.")


class Programmer(Employee):

    def programmingInfo(self):
        print("This employee is good at programming.")


class SeniorProgrammer(Programmer):

    def seniorInfo(self):
        print("This is a senior programmer.")


person = SeniorProgrammer()

person.employeeInfo()
person.programmingInfo()
person.seniorInfo()
