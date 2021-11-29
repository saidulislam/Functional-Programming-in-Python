a = [2, 5, 7, 1] 
print(min(a)) # 1 

a = [[1, 2, 3], [1, 1, 5], [6, 7, 8], [1, 1, 5]] 
print(min(a)) # [1, 1, 5]

a = [] 
print(min(a, default=0)) # 0 


a = [2, 5, 7, 1] 
print(min(a, default=0)) # 1 

# key argument
# min has an optional argument, key, that can be 
# used to modify the comparison order. It is a 
# keyword-only argument and works in the same 
# way as the sorted function. Here is a simple 
# example using a lambda function that returns 
# the third element of the item:
a = [[1, 2, 3], [1, 1, 5], [6, 7, 8], [1, 1, 5]] 
print(min(a, key=lambda x: x[2])) # [1, 2, 3] 