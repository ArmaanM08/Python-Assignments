class Circle:
    def draw(self):
        print("Drawing a circle.")

class Square:
    def draw(self):
        print("Drawing a square.")

class Triangle:
    def draw(self):
        print("Drawing a triangle.")

# Example Usage
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()