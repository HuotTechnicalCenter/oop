class Cat:
    """ This is the beginning of a class for the humble house cat
            Attributes:
            name
            weight

            Next tasks
            create one method that modifies an attribute of your dog (for example gain weight)

            create one method that returns a value

            be sure that you have an init method

            create a method that takes another object as an argument, and returns a boolean value

create a function that will print a description of your dog
            
"""
    foodDishLevel = 100
    
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def add_weight(self, weight):
        """ modifies the value of the attribute weight """
        self.weight += weight

    def rtn_weight(self):
        if self.weight > 0:
            return str(self.weight)
        else:
            return "Weight is unknown"

    def eat(self):
        Cat.foodDishLevel -= 10

    def compare_weights(self, other):
        return self.weight < other.weight

    def print_cat(self):
        print("This cat's name is: {}".format(self.name) )

c = Cat('Fluffy')


x = Cat('Spike')

print(x.rtn_weight())
x.weight = 3
print(x.rtn_weight())
x.add_weight(9)
print(x.rtn_weight())

print(c.name)

print(x.name)
print(x.weight)

x.eat()
print(c.foodDishLevel)
print(x.foodDishLevel)

y = Cat('Svetlana', 6)
print(y.rtn_weight())

print(str(x.compare_weights(y)))
if x.compare_weights(y):
    print('Svetlana weighs more than Spike')
else:
    print('Svetlana  does not weigh more than Spike')
    print('Svetlana could weigh the same or less')
    
y.print_cat()

