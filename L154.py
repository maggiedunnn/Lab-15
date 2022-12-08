class Fabric:
    def __init__(self, countryoforigin, color):
        self.countryoforigin = countryoforigin
        self.color = color
    def __str__(self):
        return self.countryoforigin + "(" + str(self.color) + ")"

F1 = Fabric("Italy", "red")
print(F1)
