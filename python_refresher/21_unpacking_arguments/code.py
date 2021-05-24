def mulitply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(mulitply(1, 3, 5))

def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

nums2 = {"x": 15, "y" : 25}
print(add(**nums2))






def apply(*args, operator):
    if operator == "*":
        return mulitply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provide to apply()"


print(apply(1, 3, 4, 5, operator = "+"))
