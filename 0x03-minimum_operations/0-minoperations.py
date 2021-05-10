#!/usr/bin/python3
"""
Minimum amount of operations
"""


def minOperations(n):
    """Minimum amount of operations"""
    count = 0
    mini = 2

    if n <= 1:
        return count
    else:
        while mini < n + 1:
            while (n % mini == 0):
                count = count + mini
                n = n / mini
            mini = mini + 1
    return count
