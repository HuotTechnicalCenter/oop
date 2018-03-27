class Cat:
    """ This is the beginning of a class for the humble house cat
            Attributes:
            name
            weight
            
"""
    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        Cat.foodDishLevel -= 10


c = Cat('Fluffy')
# c.name = "Fluffy"

x = Cat('Spike')
# x.name = "Spike"

x.add_weight(12)
# x.add_wieght(12)

print(c.name)

print(x.name)
print(x.weight)

x.eat()
print(c.foodDishLevel)
print(x.foodDishLevel)
