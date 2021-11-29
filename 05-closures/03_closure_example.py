# Convert a character into a hex string

# There are two functions in Python that you can use to do this. 
# ord converts a character to an int value representing its ASCII 
# code (or more generally its Unicode value). hex converts an int 
# value into a hex string. Using these two functions, we can define 
# a function that does the task for us, as shown below.

def codestr(c): 
    return(hex(ord(c))) 
    
h = codestr('a') 
print(h) # '0x61' 



# First, we define a compose function. compose accepts two functions, 
# f and g. It returns a function that applies g to x and then applies 
# f to the result. This is a completely generic function that can be 
# used to compose any two functions you want.

def compose(f, g): 
    def fn(x): 
        return f(g(x)) 
    return fn 
    
codestr = compose(hex, ord) 
h = codestr('a') 
print(h) # '0x61' 


# Another advantage is that we can use compose to create anonymous 
# functions. For example, we can use map to apply our composed 
# function to a string and produce a list of hex values. This saves 
# us an ugly lambda expression.
def compose(f, g): 
    def fn(x): 
        return f(g(x)) 
    return fn 

s = 'xyz' 
b = map(compose(hex, ord), s) 
print(list(b)) # ['0x78', '0x79', '0x7a'] 


# another example
import math
def compose(f, g): 
    def fn(x): 
        return f(g(x)) 
    return fn 

b = compose(lambda x: x*x, math.sin)
print(b(2))