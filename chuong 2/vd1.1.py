class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Con mèo tên " + self.name

    def __repr__(self):
        return "Cat(name='" + self.name + "')"

class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Con mèo tên " + self.name

    def __repr__(self):
        return "Cat(name='" + self.name + "')"

c = Cat("Miu")

   # gọi __str__
print(c)          # gọi __repr__ (trong interactive)
