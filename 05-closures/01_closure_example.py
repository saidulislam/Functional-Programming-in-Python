def make_print(): 
  
  def print_hello(): 
    print('hello') 

  return print_hello

fn = make_print()
fn()

# What is a closure?
# So, what is a closure? A closure normally requires three things:

# An outer function that contains an inner function.
# The outer function has parameters and/or local variables.
# The outer function returns the inner function as a function object.

# In fact, strany parameters (e.g., our make_print function near the 
# start of this lesson). However, a closure is not very useful if there 
# is no way to vary the behavior of the closure.


# A closure
def make_printx(x): 

    def printx(): 
        print(x) 

    return printx

# Main code 
fn1 = make_printx(7) 
fn2 = make_printx(100) 
fn1() 
fn2()

# A more useful closure
def make_printb(start, end): 

  def printb(s): 
    print(start + s + end) 

  return printb

# Main code 
sq = make_printb('[', ']') 
sq('hello')

dbl_ang = make_printb("<<", ">>")
dbl_ang('hello')