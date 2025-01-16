class Car:
    def __init__(self, make="Unknown", model="Unknown", year=2000):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car: {self.make}, Model: {self.model}, Year: {self.year}")


car = Car()
car.display_details()