a = ('red', 'green', 'blue')

for i, color in enumerate(a):
    print(i, color)


a = ('red', 'green', 'blue')
for color in enumerate(a):
    print(color)


# optional start value
a = ('red', 'green', 'blue') 
for i, s in enumerate(a, 1): 
    print(i, s)