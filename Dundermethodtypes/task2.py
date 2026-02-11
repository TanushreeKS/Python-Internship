class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model


m1 = Mobile("Apple", "iPhone15", 80000)
m2 = Mobile("Apple", "iPhone15", 90000)
m3 = Mobile("Samsung", "S23", 70000)

print(m1 == m2)
print(m1 == m3)
