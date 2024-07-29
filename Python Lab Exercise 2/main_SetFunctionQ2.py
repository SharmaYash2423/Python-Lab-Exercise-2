from module_SetFunctionQ2 import addElem, removeElem, unionSet, intersectionSet, diffSet, checkSubset, calcLength, symmetricDifference, powerSet, getAllSubsets

set1 = {5, 6, 7}
set2 = {7, 8, 9}

# Adding an element
addElem(set1, 8)  # Adding element 8 to set1
print(set1)  # Output: {5, 6, 7, 8}

# Removing an element
removeElem(set1, 6)  # Removing element 6 from set1
print(set1)  # Output: {5, 7, 8}

# Union
union_result = unionSet(set1, set2)  # Union of set1 and set2
print(union_result)  # Output: {5, 7, 8, 9}

# Intersection
intersection_result = intersectionSet(set1, set2)  # Intersection of set1 and set2
print(intersection_result)  # Output: {7, 8}

# Difference
diff_result = diffSet(set1, set2)  # Difference of set1 from set2
print(diff_result)  # Output: {5}

# Check subset
is_subset = checkSubset({5, 7}, set1)  # Checking if {5, 7} is a subset of set1
print(is_subset)  # Output: True

# Calculate length
length = calcLength(set1)  # Calculating the length of set1
print(length)  # Output: 3

# Symmetric difference
symmetric_diff = symmetricDifference(set1, set2)  # Symmetric difference of set1 and set2
print(symmetric_diff)  # Output: {5, 9}

# Power set
power_set_result = powerSet(set1)  # Power set of set1
print(power_set_result)  # Output: {frozenset(), frozenset({5}), frozenset({7}), frozenset({8}), frozenset({5, 7}), frozenset({5, 8}), frozenset({7, 8}), frozenset({5, 7, 8})}

# Get all subsets
all_subsets_result = getAllSubsets(set1)  # All subsets of set1
print(all_subsets_result)  # Output: [{}, {5}, {7}, {8}, {5, 7}, {5, 8}, {7, 8}, {5, 7, 8}]
