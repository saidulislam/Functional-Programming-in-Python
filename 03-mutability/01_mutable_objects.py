def evil_func(x): 
    x[0] = 0 

k = [1, 2, 3] 
evil_func(k) 
print(k) # [0, 2, 3] 


# Defensive copying
def evil_func(x): 
    x[0] = 0 

k = [1, 2, 3]
evil_func(list(k)) 
print(k) # [1, 2, 3] 

# Immutability is the answer
def evil_func(x): 
  x[0] = 0 

t = (1, 2, 3) 
evil_func(t) 
print(t) 
