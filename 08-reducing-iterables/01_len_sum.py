# len
print(len([1, 2, 30])) # 3 
print(len('uvwxyz')) # 6

# sum
a = [2, 5, 7, 1] 
print(sum(a)) # 15 

# You can supply an optional start value to sum. 
# It will just get added to the total.
a = [2, 5, 7, 1] 
print(sum(a, -3)) # 12


a = [[2, 4], [0, 0], [5, 3]] 
# print(sum(a)) # ERROR you cannot do that

# but you can do the following
a = [[2, 4], [0, 0], [5, 3]] 
print(sum(a, [])) # [2, 4, 0, 0, 5, 3]  


# to add strings, you can use join
a = ['abc', 'pqr', 'xyz'] 
s = ''.join(a)
print(s)
