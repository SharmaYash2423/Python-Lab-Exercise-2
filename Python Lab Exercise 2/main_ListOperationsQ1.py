# main_ListOperations.py

from module_ListFunctionsQ1 import find_maximum, find_minimum, calculate_sum, compute_average, determine_median

# Example usage with list comprehensions
numbers = [x for x in range(1, 11)]
print("Max:", find_maximum(numbers))
print("Min:", find_minimum(numbers))
print("Sum:", calculate_sum(numbers))
print("Average:", compute_average(numbers))
print("Median:", determine_median(numbers.copy()))
