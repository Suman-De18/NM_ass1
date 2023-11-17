import timeit
import fibonacci

# Measure the time taken to generate 100 Fibonacci numbers
execution_time = timeit.timeit('fibonacci.generate_fibonacci(100)', setup='import fibonacci', number=1)
print(f"Time taken to generate 100 Fibonacci numbers: {execution_time:.6f} seconds")
