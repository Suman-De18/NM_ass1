# We can convert the previous code into a Python module that contains a function to generate n Fibonacci numbers:
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:n]
