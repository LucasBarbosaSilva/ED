def fibonacci(n):
    fib = 0
    if(n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(15))