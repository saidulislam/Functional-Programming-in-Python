# Example 1
t = (10,20,30,40,50)
u = t
print(t[2])
print(u[2])

# Example 2
def square(x):
    return x*x

sq = square
a = 3
print(sq(a))

# Example 3
pr = print
pr('This is another alias')

# Example 4
def a():
    print(1)

def b():
    a()

b()

def a():
    print(2)

b()