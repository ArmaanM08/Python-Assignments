class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

# Example Usage
product = Product()
product.price = 50
print(product.price)