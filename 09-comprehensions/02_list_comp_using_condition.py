import math
k = [-1, 16, 9, -4, 0, 25]

a = [ math.sqrt(x) for x in k if x >= 0]
print(a)