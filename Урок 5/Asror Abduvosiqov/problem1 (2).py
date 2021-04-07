
# думаю тут коментарий не надо так как тут все очень просто и легко
class Cricle:
    def __init__(self):
        self.r = 0
        self.p = 3.14
    def func(self):
        self.perimetr = 2 * self.p * self.r
        self.s = self.p * (self.r ** 2)
        print(self.s, self.perimetr)
a = Cricle()
a.r = 8
a.func()
