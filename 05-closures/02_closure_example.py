a = [2.2, 5.6, 1.9, 0.1, 2.3] 
b = map(round, a) 
# print(b)
print(list(b)) # [2, 6, 2, 0] 

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))


# Using a closure instead of a lambda
def double_num():

    def double_it(x):
        return x*2

    return double_it

a = [1,2,3,4,5]
b = map(double_num(), a)
print(list(b))

