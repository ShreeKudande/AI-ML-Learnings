#Q. Design & create an online store for Products (name, price).
#Track toltal products being created.
#Create a static method to calculate discount on each product based on a % parameter.

class Product:

    count  = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    @staticmethod
    def calc_discount(price, discount):
        final_discount = price - (discount * price/100)
        print(f"Final price after discount is {final_discount}")

P1 = Product("Phone", 10_000)
P2 = Product("Laptop", 10_0000)
P3 = Product("Pen", 10)

P1.get_info()
P2.get_info()
P3.get_info()

Product.get_count()

P1.calc_discount(P1.price, 12)

#Output :-
# Price of Phone is 10000
# Price of Laptop is 100000
# Price of Pen is 10

# total products in store = 3

# Final price after discount is 8800.0

