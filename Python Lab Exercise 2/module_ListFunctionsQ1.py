# module_ListFunction.py

def find_maximum(lst):
    """Find the maximum value in a given list."""
    return max(lst)

def find_minimum(lst):
    """Find the minimum value in a given list."""
    return min(lst)

def calculate_sum(lst):
    """Calculate the sum of all elements in a list."""
    return sum(lst)

def compute_average(lst):
    """Compute the average of the list."""
    return sum(lst) / len(lst) if len(lst) > 0 else 0

def determine_median(lst):
    """Determine the median of a list."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
