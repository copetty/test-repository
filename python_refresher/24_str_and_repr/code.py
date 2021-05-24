class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # used to print out string representation of object
        return f"Person {self.name}, {self.age} years old"

    def __repr__(self):# used to print out unambiguous representation of the object like for debugging
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)

print(bob)