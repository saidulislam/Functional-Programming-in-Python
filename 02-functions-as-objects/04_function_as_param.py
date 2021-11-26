# Example 1
def inch2cm(x): 
    return x*2.54

def convert(x):
    y = inch2cm(x)
    print(x, '=>', y)

convert(3)

# Example 2
def inch2cm(x): 
    return x*2.54

def convert(f, x):
    y = f(x)
    print(x, '=>', y)

convert(inch2cm, 3)

# Example 3
def convert(f, x): 
    y = f(x) 
    print(x, '=>', y) 

def c2f(x): 
    return x*1.8 + 32 
    
convert(c2f, 18) # 18 => 64.4

# Example 4
def convert(f, x): 
    y = f(x) 
    print(x, '=>', y) 

def c2f(x): 
    return x*1.8 + 32 
    
convert(c2f, 18) # 18 => 64.4 

# Example 5
def i2text(x): 
    text = ['zero', 'one', 'two', 'three'] 
    return text[x] 
    
convert(i2text, 2) # 2 => two 

# Example 6
p = [3, 7, 2, 6, 1]
q = sorted(p) 
print(q) # [1, 2, 3, 6, 7]


# Example 7
p = ['red', 'green', 'blue', 'yellow', 'cyan'] 
q = sorted(p) 
print(q) # ['blue', 'cyan', 'green', 'red', 'yellow']


# Example 8
def area(x): 
    return x[0]*x[1] 

p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)] 
# Each tuple will be passed into the area function. 
# This function multiplies the first and the second 
# element of the tuple (the width and height) to give 
# the area. The area is then used as the sort criterion. 
# As you can see from the result, this sorts the 
# rectangles in order of area.
q = sorted(p, key=area) 
print(q) # [(2, 2), (1, 7), (4, 2), (3, 3), (5, 2)] 


# Example 9
def add1(): 
    return lambda x: x + 1 

f = add1() 
print(f(2))

sqr_it = lambda x: x*x
print(sqr_it(5))

# Example 10
# in-place calling
a = (lambda x: x*x)(9)
print(a)
