a = [3, 2, 1, 6, 7, 0]

f = filter(lambda x: x%2 == 0, a)
print(list(f)) # prints only the even number



strings = ('red', '', 'green', '', 'blue') 
for s in filter(len, strings): 
    print(s) # prints non empty strings