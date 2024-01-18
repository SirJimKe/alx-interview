#!/usr/bin/python3
"""
Minumum operations function
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n H characters.
    """
    if n == 1:
        return 0

    operations = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
