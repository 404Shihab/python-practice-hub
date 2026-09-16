class Car:
    name="civic"
    brand = "honda"
    topSpeed = "200"

    def getInfo(self):
        print(f"Name: {self.name}. brand: {self.brand}. top speed: {self.topSpeed}")
    @staticmethod
    def greet():
        print("Good morning sir")

c = Car()
c.name="city"
Car.getInfo(c)
# c.greet()
# Car.greet(c)
c.greet()