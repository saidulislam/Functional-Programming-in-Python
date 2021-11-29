def mult3(a, b, c): 
    return a*b*c 

x = mult3(2, 3, 5) # 30 
print(x)


# unpacking with *p
def mult3(a, b, c): 
    return a*b*c 

p = [2, 3, 5] 
x = mult3(*p) # equivalent to mult3(2, 3, 5)

print(x)


# same as the above code section
a = [2.2, 5.6, 1.9] 
b = map(round, a) 
x = mult3(*b) # equivalent to mult3(2, 6, 2) 

print(x)


# another example of unpacking
a = [2.2, 5.6, 1.9] 
b = map(round, a) 
k = [*b] # k is [2, 6, 2]
print(k)


# alternative to using the list function
a = [2.2, 5.6, 1.9] 
b = map(round, a) 

t = (*b,) # t is (2, 6, 2) 
print(t)

b = map(round, a) 
s = {*b} # s is {2, 6} 
print(s)


# extended unpacking
a = range(3) 
b = range(4, 7) 
k = [*a, 10, *b] # [0, 1, 2, 10, 4, 5, 6]
print(k)

