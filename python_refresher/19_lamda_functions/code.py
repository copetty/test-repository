def add(x, y):
    return x + y

add2 = lambda x, y: x + y # same as add function




print(add(5,7))
print(add2(5,7))




def double(x):
    return x * 2

double3 = lambda x : x * 2

sequence = [ 1, 3, 4, 9]
double = [double(x) for x in sequence] # doubles with list comprehension, list comprehension is faster than map

doubled2 = list(map(double, sequence)) # same as double but using map, need to put it inside a list to print it
