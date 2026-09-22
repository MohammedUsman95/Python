class Product:

    def __init__(self, t, p, q, d):
        self.title = t
        self.price = p
        self.quantity = q
        self.discount = d


    def total(self):
        return self.price * self.quantity

    def apply_discount(self):
        discount = self.price * self.discount / 100
        self.price = self.price - discount

    def get_discounted_price(self):
        discount = self.price * self.discount / 100
        return self.price - discount

    def get_discounted_total(self):
        return self.get_discounted_price() * self.quantity

    def display(self):
        print()
        print("Product Details\n--------------------")
        print("Name =", self.title)
        print("Price =", self.price)
        print("Quantity =", self.quantity)
        print("Total =", self.total())
        print("Discounted Price =", self.get_discounted_price())
        print("Discounted Total =", self.get_discounted_total())

product1 = Product("Mobile", 20000, 10, 0)
product1.display()
