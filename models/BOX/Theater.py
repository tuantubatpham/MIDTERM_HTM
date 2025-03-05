class Theater:
    def __init__(self,ThId, location,capacity):
        self.ThId = ThId
        self.location = location
        self.capacity = capacity
    def __str__(self):
        return f"{self.ThId}\t{self.location}\t{self.capacity})"