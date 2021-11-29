def countdown(start):
  # This is the outer enclosing function
  def display():
    # This is the nested function
    n = start
    while n > 0:
      n-=1
      print('T-minus %d' % n)
 
  display()


# We execute the function
countdown(3)


# *******************************
# Defining a Closure Function

def countdown(start):
  # This is the outer enclosing function
  def display():
    # This is the nested function
    n = start
    while n > 0:
      n-=1
      print('T-minus %d' % n)
  return display

# Now let's try calling this function.
counter1 = countdown(2)
counter1()


# When to use closures?
# When there are few methods (one method in most cases) to be implemented 
# in a class, closures can provide an alternate and more elegant solution.

from urllib.request import urlopen
def page(url): 
  def get(): 
    return urlopen(url).read() 
  return get

url1 = page("http://www.google.com") 
url2 = page("http://www.bing.com") 
url1
# <function page.<locals>.get at 0x10a6054d0>
url2
# <function page.<locals>.get at 0x10a6055f0>
  
gdata = url1()     # Fetches http://www.google.com
print(gdata)

bdata = url2()     # Fetches http://www.bing.com