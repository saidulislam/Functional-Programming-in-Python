first = ('John', 'Anne', 'Mary', 'Peter') 
last = ('Brown', 'Smith', 'Jones', 'Cooper') 
age = (25, 33, 41, 28)

# zip accepts a set of iterables and transforms 
# them into an iterator of tuples, as shown below.
z = zip(first, last, age)
print(list(z))

for f, l, a in zip(first, last, age):
    print(f, l, a)


# Stream with different lengths
# Incidentally, if the original streams have different lengths, 
# zip will terminate when the shortest stream is exhausted, 
# as shown below.

a = (10, 11, 12) 
b = (20, 21) 
c = (30, 31, 32, 33)

z = zip(a, b, c) 
print(list(z))

# reversing the zip
a = (10, 11, 12, 13) 
b = (20, 21, 22, 23) 
c = (30, 31, 32, 33) 

z = zip(a, b, c) 
restored = zip(*z) 
print(list(restored)) 