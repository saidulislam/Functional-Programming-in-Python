listofzeros = [1,0] * 500 # list containing a 1000 values
myiter = iter(listofzeros)
print(myiter)

for x in myiter: 
  print(x)
  if x==0: 
    break 