class Car:
    name="civic"
    brand = "honda"
    topSpeed = 300

    def __init__(self, name, brand, topSpeed): #this is dunder method , which is automatically called 
        print("this is a constructor")
        self.name = name
        self.brand=brand
        self.topSpeed=topSpeed

    def getInfo(self):
        print(f"Name: {self.name}, brand: {self.brand}, top speed: {self.topSpeed}")
    @staticmethod
    def greet():
        print("Good morning sir")

c = Car("accord", "Honda", 200)
# c.name="city"
Car.getInfo(c)
# c.greet()
# Car.greet(c)
c.greet()


