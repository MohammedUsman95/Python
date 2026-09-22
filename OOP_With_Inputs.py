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


p1_t = input("Enter The Product Name: ")
p1_p = int(input("Enter The Cost: "))
p1_q = int(input("Enter The quantity: "))
p1_d = int(input("Enter The Discount %: "))

print()

p2_t = input("Enter The Second Product Name: ")
p2_p = int(input("Enter The Second Product Cost: "))
p2_q = int(input("Enter The Second Product Quantity: "))
p2_d = int(input("Enter The Second Product Discount %: "))

product1 = Product(p1_t, p1_p, p1_q, p1_d)
product1.display()

product2 = Product(p2_t, p2_p, p2_q, p2_d)
product2.display()
