def named(** kwargs):
    print(kwargs)

named(name="Bob", age=25)

def named2(name, age):
    print(name, age)

details = {"name": "Bob", "age" : 25}
named2(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name= "Bob", age = 25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)
       #*args is for positional arguments, **kwargs is for named arguments


both(1, 3, 5, name = "Bob", age = 25)


def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Bob") will throw in error
# myfunction(**None) will throw an error **kwargs must take in a dictionary it is for name arguments