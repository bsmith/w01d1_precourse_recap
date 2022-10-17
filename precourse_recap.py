"""Three fibonacci implementations
"""

import inspect
import math

print("Three fibonacci implementations")

def fib1(n):
    """fib1 implements a simple recursive fibonacci function"""
    if n in (1, 2):
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    """fib2 implements a iterative fibonacci function"""
    prev,prev2 = 1, 1
    while n > 2:
        prev,prev2 = prev + prev2, prev
        n = n - 1
    return prev

def fib3(n):
    """fib3 implements the closed form formula"""
    phi = (1.0 + math.sqrt(5.0))/2.0
    return int((phi**n - (1-phi)**n)/math.sqrt(5))

def fib4(n):
    """fib4 recurses but only once per level"""
    def helper(prev, prev2, n):
        if n == 1:
            return prev2
        elif n == 2:
            return prev
        else:
            return helper(prev + prev2, prev, n - 1)
    return helper(1, 1, n)

numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 100]
functions = [fib1, fib2, fib3, fib4]

for idx, func in enumerate(functions):
    description = inspect.getdoc(func)
    print("")
    print(f"Method number {idx+1}: {description}")
    for num in numbers:
        if (num > 25 and idx == 0):
            print(f"Skipping Fib[{num}] as it's too slow")
            continue
        result = func(num)
        print("Fib[" + str(num) + "] = " + str(result))

print("Finished")
