class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimetr(self):
        return self.radius * 2 * 3.14

newCircle = Circle(8)
print("Area:", newCircle.area(), "\nPerimetr:", newCircle.perimetr())