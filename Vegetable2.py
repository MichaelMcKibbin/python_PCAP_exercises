class Vegetable:
    def __init__(self, weight, price, origin):
        self.weight = weight
        self.price = price
        self.origin = origin

        self.weight = 5.00

    def getWeight(self):
        return self.weight


    def __str__(self):
        return "weight"+str(self.weight)+", price"+str(self.price)+", origin"+str(self.origin)


class Onion(Vegetable):
    def __init__(self, weight, price, origin):
      super().__init__(weight, price, origin)


onion2 = Onion(1.99, 2.99, "USA")
print(onion2.getWeight())
print(onion2)


class Vegetable2:
    pass

class Potato(Vegetable2):
    pass

print(isinstance(Potato, Vegetable2))
potato=Potato()
print(isinstance(potato, Potato))
print(isinstance(potato, Vegetable2))
print(issubclass(Potato, Vegetable))

# print(issubclass(potato, Potato))
print(issubclass(Potato, Vegetable2))
print(issubclass(Vegetable2, object))
