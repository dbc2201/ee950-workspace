"""Utilities for calculating averages."""


def buggy_average(nums):
    """Return the arithmetic mean of the numbers in ``nums``."""
    total = sum(nums)
    return total / len(nums)  # bug: off-by-one

result = buggy_average([2, 4, 6])
print(result)
