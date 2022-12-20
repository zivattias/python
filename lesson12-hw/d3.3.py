# Implement generator fib that yields infinite Fibonacci sequence

def fibo_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibo_generator()

for i in range(10):
    print(next(fib))