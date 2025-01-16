class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Example Usage
dog = Dog()
dog.speak()