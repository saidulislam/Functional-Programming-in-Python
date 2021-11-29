import sys

print("Limit: ", sys.getrecursionlimit())

# sys.setrecursionlimit(1500)

def add_all_prior_numbers(n):
    assert n > 0 and int(n) == n, "The number needs to be a positive integer."

    if n == 1:
        return 1
    else:
        return n + add_all_prior_numbers(n-1)

print(add_all_prior_numbers(10))