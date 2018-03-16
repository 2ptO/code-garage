# Write a function fib() that takes an integer n and returns the
# nth Fibonacci number.

# Let's say our Fibonacci series is 0-indexed and starts with 0. So:
# fib(0) = 0
# fib(1) = 1
# fib(2) = 1
# fib(3) = 2

def fib(n):
    if n < 0:
        raise ValueError("Cannot generate fibonacci series for negative numbers")

    a, b = 0, 1
    if n in [0, 1]:
        return n
    
    # since we answered the cases of n=0 and n=1 above, now
    # start find fib values greater n. In other words, loop
    # from 2 to n
    while n > 1:
        a, b = b, a+b
        n -= 1

    return b

# I too started with recursive solution mind, but the fact of duplicate
# work and expense of call stack struck me immediately, so switched
# to iterative solution instead. 