from numpy.f2py.symbolic import number_types


class Beverage:
    def __init__(self, BName, BQuantity, BPrice):
        self.BName=BName
        self.BQuantity=BQuantity
        self.BPrice=BPrice
    def __str__(self):
        return f"{self.BName}\t{self.BQuantity}\t{self.BPrice}"