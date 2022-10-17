import inspect
import math

print("Three fibonacci implementations")

# TODO: Complete implementation of fib1
def fib1(n):
    """fib1 implements a simple recursive fibonacci function"""
    return -1

# TODO: Complete implementation of fib2
def fib2(n):
    """fib2 implements a iterative fibonacci function"""
    return -1

def fib3(n):
    """fib3 implements the closed form formula"""
    phi = (1.0 + math.sqrt(5.0))/2.0
    return int((phi**n - (1-phi)**n)/math.sqrt(5))

numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 100]
functions = [fib1, fib2, fib3]

for idx in range(0, len(functions)):
    func = functions[idx]
    description = inspect.getdoc(func)
    print("")
    print(f"Method number {idx+1}: {description}")
    for num in numbers:
        result = func(num)
        print("Fib[" + str(num) + "] = " + str(result))

print("Finished")