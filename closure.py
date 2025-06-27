from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Save to cache and return Fibonacci numbers"""
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Get function fibonacci
fib = caching_fibonacci()
# Use fibonacci to get Fibonacci numbers
print(fib(10))
print(fib(15))
