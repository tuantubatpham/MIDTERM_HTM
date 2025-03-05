from PIL.ImImagePlugin import number
from numpy.f2py.symbolic import number_types


class Popcorn:
    def __init__(self, PName, PQuantity, PPrice):
        self.PName=PName
        self.PQuantity=PQuantity
        self.PPrice=PPrice
    def __str__(self):
        return f"{self.PName}\t{self.PQuantity}\t{self.PPrice}"