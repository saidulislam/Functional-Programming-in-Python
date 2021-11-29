

# def RecursiveFunction() :
#   # Base Case
#   if <baseCaseCondition> : #sets target state
#     <return some base case value>
#   # Recursive Case
#   else :
#     <return(recursive call and any other task)>

def factorial(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number is defined for non-negative indices only!'
    if n in [0,1]:
        # base case condition
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-6))