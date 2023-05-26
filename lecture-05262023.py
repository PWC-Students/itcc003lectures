# Introduction to classes and objects
# PascalCasing - we follow this casing in naming your classes
# camelCasing - we follow this casing for creating variables and functions

class Person:
    # a constructor is used to initialize the attributes of the object. The constructor method has a predefined name __init__().
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is" + self.name + "and I am " + str(self.age) + "years old.")

    def talk(self):
        print("John is talking.")

    def read(self, book, page):
        print("John is reading " + book + " and is on page " + str(page))

johnDoe = Person("John Doe", 25)
marieDoe = Person("Marie Doe", 35)

johnDoe.greet()
johnDoe.read("How to Kill a Mocking Bird", 23)

