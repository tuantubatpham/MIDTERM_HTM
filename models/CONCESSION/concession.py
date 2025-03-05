class CON:
    def __init__(self, popcorn, beverage, combo, total_price):
        self.popcorn = popcorn
        self.beverage = beverage
        self.combo = combo
        self.total_price = total_price

    def __str__(self):
        return f"Order: Popcorn={self.popcorn}, Beverage={self.beverage}, Combo={self.combo}, Total Price={self.total_price}"

print(CON)