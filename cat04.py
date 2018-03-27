class Cat:
    """ This is the beginning of a class for a house cat
    attributes:
        name
        weight

    """


    def __init__(self, name, weight = None):
        """The init method has a default value of None for weight"""
        self.name = name
        self.weight = weight

    def add_weight(self, weight):
        self.weight = weight

    def get_name(self):
        print('We are about to return the cat\'s name')
        return self.name
        print("This will never print because it is after the return")


c = Cat('Fluffy')
# c.name = "Fluffy"

x = Cat('Spike')
# x.name = "Spike"

y = Cat("Shaggy", 8)

x.add_weight(12)
print(c.name)

print(x.name)
print(y.name)

catName = y.get_name()
print("The cat's name is: {} \n".format(catName))
