class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car: {self.make}, Model: {self.model}, Year: {self.year}")


car = Car("Toyota", "Corolla", 2020)
car.display_details()