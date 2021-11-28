def tail(x): 
  if x: # If x is already empty do nothing 
    del x[0] 

k = [1, 2, 3] 
# The tail function takes a list and returns a list 
# that is identical except that the first term is removed
tail(k)
print(k) # [2, 3] 

def tail(x): 
  return x[1:] 

t = (1, 2, 3) 
t = tail(t) 
print(t) # (2, 3)

# using slices
v = (1,2,4)
n = 2

u = v[:n] + (3,) + v[n:] 
print(u)

v = (1,2,3,4,5)
n = 2

u = v[:n] + v[n+1:] 
print(u)


my_string = "hppy"
n = 1

u = my_string[:n] + "a" + my_string[n:] 
print(u)

# using list comprehension
v = (1,5,7)

u = [x + 1 for x in v] 
t = tuple(u) 
print(t)

# using the for loop
v = (1,0,2,0,5)
u = [] 
for x in v: 
  u.append(x) 
  if x == 0: 
    u.append(x) 
t = tuple(u) 
print(t)