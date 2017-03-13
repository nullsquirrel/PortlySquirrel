""" stats.py
Library containing basic statistical math functions
"""

def mean(values):
    """ Returns the mean of values """
    return sum(values) / len(values)

def median(values):
    """ Finds the middle most value of values """
    num = len(values)
    sorted_vals = sorted(values)
    midpoint = num // 2

    if num % 2 == 1:
        return sorted_vals[midpoint]
    else:
        low = midpoint - 1
        high = midpoint
        return (sorted_vals[low] + sorted_vals[high]) / 2
