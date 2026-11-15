class Vegetable:

    def __init__(self, weight,price,origin):
        self.weight = weight
        self.price = price
        self.origin = origin

class Onion(Vegetable):

    def __init__(self, weight, price, origin):
        super().__init__(weight, price, origin)


    def __str__(self):
        return f"Onion(weight={self.weight}, price={self.price}, origin={self.origin})"

onion1 = Onion(1.5, 2.0, "USA")
# print(onion1.__name__)
print("16" + Onion.__name__)
print("17" + onion1.__module__)
print("18" + Onion.__module__)
print(Onion.__bases__)
# print(onion1.__bases__)




