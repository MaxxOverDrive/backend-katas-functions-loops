#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Matt Williams"


def add(x, y):
    """Add two integers."""
    return x + y


print(add(2, 4))


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    s = 0
    for i in range(abs(x)):
        s = add(s, y)
    return s if x > 0 else -s


print(multiply(6, -8))


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    t = 1
    for i in range(n):
        t = multiply(x, t)
    return t


print(power(2, 8))


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    t = 0
    if x > 0:
        for i in range(x, 0, -1):
            if t == 0:
                t = i
            else:
                t = multiply(t, i)
        return t
    else:
        return 1


# print(factorial(4))


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    f = []
    if n <= 1:
        return n
    for i in range(n):
        if len(f) <= 1:
            f.append(i)
        else:
            f.append(add(f[i - 2], f[i - 1]))
    return add(f[-2], f[-1])


# print(fibonacci(8))


if __name__ == '__main__':
    # your code to call functions above
    pass
