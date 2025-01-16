class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


dog = Dog("Buddy")
dog.speak()