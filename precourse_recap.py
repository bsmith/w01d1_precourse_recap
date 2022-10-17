import inspect

print("Three fibonacci implementations")

# TODO: Complete implementation of fib1
def fib1(n):
    """fib1 implements a simple recursive fibonacci function"""
    if (n in (1, 2)):
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

# TODO: Complete implementation of fib2
def fib2(n):
    """fib2 implements a iterative fibonacci function"""
    return -1

def fib3(n):
    """fib3 implements the closed form formula"""
    return -1

numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 100]
functions = [fib1, fib2, fib3]

for idx in range(0, len(functions)):
    func = functions[idx]
    description = inspect.getdoc(func)
    print("")
    print(f"Method number {idx+1}: {description}")
    for num in numbers:
        if (num > 25 and idx == 0):
            continue
        result = func(num)
        print("Fib[" + str(num) + "] = " + str(result))

print("Finished")