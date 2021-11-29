def square(x):
    return x*x

a = [2,3,4]
m = map(square, a)

print(list(m))


# map with more than one parameter
import operator 

a = [20, 30, 40] 
b = range(3) # [0,1,2]
m = map(operator.sub, a, b) # subtract b from a

print(list(m))