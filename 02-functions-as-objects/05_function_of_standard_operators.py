import operator

a=5
b=2

x = operator.add(a, b)       # Equivalent to x = a + b
print(x)

x = operator.truediv(a, b)   # Equivalent to x = a / b 
print(x)

x = operator.floordiv(a, b)  # Equivalent to x = a // b
print(x)

# partials
from functools import partial 

f = partial(operator.add, 3) 
x = f(4) # Equivalent to x = 3 + 4 
print(x)

