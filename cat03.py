class Cat:
    """ This is the beginning of a class for the humble house cat """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight


c = Cat('Fluffy')
# c.name = "Fluffy"

x = Cat('Spike')
# x.name = "Spike"

x.add_weight(12)
# x.add_wieght(12)

print(c.name)

print(x.name)
print(x.weight)
