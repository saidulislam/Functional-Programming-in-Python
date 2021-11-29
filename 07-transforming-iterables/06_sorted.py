dates = \
['2019/04/06',
'2017/04/15',
'2019/03/21', 
'2018/04/10', 
'2019/04/08', 
'2017/03/20', 
'2018/06/30', 
'2019/09/30', 
'2018/04/11', 
'2017/03/14']

# If we simply sort this list, we will get the dates 
# in ascending order (that is because we are using 
# a year/month/day format), as shown below.
sorted_dates = sorted(dates) 
print(sorted_dates)

# sort this sorted list again but just using the month field
# sorted accepts a key parameter that is a function
sorted_by_month = sorted(sorted_dates, key=lambda x: x[5:7]) 
print(sorted_by_month)


# utility key functions
people = \
[('John', 'Brown', 25), 
('Anne', 'Smith', 33), 
('Mary', 'Jones', 41), 
('Peter', 'Cooper', 28)] 

# We would like to sort them by their second names. That 
# isn’t difficult; we can just use a lambda function as 
# the key to extract the second element, as shown below.

sorted_by_surname = sorted(people, key=lambda x: x[1])  
print(sorted_by_surname)


# we will use methodcaller in a bit
fruits = ['Banana', 'apple', 'Apricot','Clementine', 'avocado']

sorted_names = sorted(fruits, key=lambda x: x.lower())
print(sorted_names)


# The above code is fine, but a better method is as follows:
from operator import methodcaller 

sorted_names = sorted(fruits, key=methodcaller('lower')) 
print(sorted_names)

# the way method caller works
f = methodcaller('lower') 
s = f('Banana') # equivalent to 'Banana'.lower() 

print(s)


# sort method
k = [1, 7, 2, 4, 1] 
k.sort() 
print(k) # [1, 1, 2, 4, 7] 