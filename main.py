"""
Memoizer
--------
Sometimes, we have computations (encapsulated in functions)
that are extremely *expensive* to compute. Our recursive
Fibonacci function is one example of this, having to
recompute every previous term recursively for every term.

A memoizer is a decorator that stores the result for a
given input in a dictionary, acting as a sort of
caching layer.
"""
import functools
import time


def memoize(function):
    results = {}

    @functools.wraps(function)
    def inner(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))  # Technique stolen from stack overflow
        try:  # Done like this instead of .get(key, None) because function could return None
            result = results[key]
        except KeyError:
            result = function(*args, **kwargs)
            results[key] = result
        return result

    return inner


@memoize
def fib(n):
    if n <= 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    start = time.perf_counter()
    fib(30)
    print(f"{time.perf_counter() - start}")
    start = time.perf_counter()
    fib(30)
    print(f"{time.perf_counter() - start}")


if __name__ == "__main__":
    main()
