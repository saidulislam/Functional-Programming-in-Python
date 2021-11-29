import functools, operator 

a = [2, 3, 5, 2] 
print(functools.reduce(operator.mul, a)) # 60 


# initial value
a = [2, 3, 5, 2] 
print(functools.reduce(lambda x, y: x*y, a, 10)) # 600

# If the iterable is empty, reduce will return 
# the value of the initializer.
a = [] 
print(functools.reduce(lambda x, y: x*y, a, 10)) 