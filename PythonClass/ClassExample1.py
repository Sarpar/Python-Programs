class MyClass:
    x = 5

p1 = MyClass()
print (p1.x)


# __init__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print("Hello " + self.name)

p1 = Person("John", 36)
print(p1.name, p1.age)
p1.printName()