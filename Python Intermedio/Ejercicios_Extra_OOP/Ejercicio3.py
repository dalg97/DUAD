class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory():
    products = []
    def add_product(self, product):
        self.products.append(product)

    def show_inventory(self):
        for product in self.products:
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
product_1 = Product("Laptop", 1000, 5)
product_2 = Product("Smartphone", 500, 10)

Inventory = Inventory()
Inventory.add_product(product_1)
Inventory.add_product(product_2)

Inventory.show_inventory()
print(f"Total inventory value: {Inventory.get_total_value()}")
