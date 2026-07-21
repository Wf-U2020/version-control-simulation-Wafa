def gen_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


# Test code
num_terms = 10

print(f"First {num_terms} Fibonacci numbers:")

for index, fib_num in enumerate(gen_fibonacci(num_terms), start=1):
    print(f"Fibonacci #{index}: {fib_num}")
    