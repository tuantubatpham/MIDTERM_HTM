class Combo:
    def __init__(self, CbName, CbQuantity, CbPrice):
        self.CbName=CbName
        self.CbQuantity=CbQuantity
        self.CbPrice = CbPrice

    def __str__(self):
        return f"{self.CbName}\t{self.CbQuantity}\t{self.CbPrice}"