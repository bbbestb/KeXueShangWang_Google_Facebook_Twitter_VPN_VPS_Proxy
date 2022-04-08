#!/usr/bin/python
# make a Fibonacci generator.


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    fib10 = fib(10)
    for i in fib10:
        print i
