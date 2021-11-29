a = [2, 5, 7, 1] 
print(max(a)) # 7 

# any accepts an iterable. It will return True 
# if any of the elements have a true value. 
# It will return False if none of the elements 
# have a true value or if the iterable is empty.

print(any([1, 0, 2]))   
print(any(['a', '', 'z']))  
print(any([0, '', False]))
print(any([]))

# all accepts an iterable. It will return True 
# if all of the elements have a true value. It 
# will return False if any of the elements have 
# a false value. Unlike any, all will return 
# True if the iterable is empty.

print(all([1, 0, 2])) 
print(all(['a', '', 'z'])) 
print(all([1, 'a', True]))
print(all([])) 