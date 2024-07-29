# main_DictOperations.py

from module_DictFunctionQ3 import merging_Dict, common_keys, invert_dict, common_key_value_pairs

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'c': 3, 'd': 5, 'e': 6}

# Merging dictionaries
print("Merging dictionaries:")
merged_dict = merging_Dict(dict1, dict2, dict3)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}

# Finding common keys
print("\nCommon keys in dictionaries:")
common_keys_result = common_keys(dict1, dict2, dict3)
print(common_keys_result)  # Output: {'c'}

# Inverting a dictionary
print("\nInverting a dictionary (dict1):")
inverted_dict = invert_dict(dict1)
print(inverted_dict)  # Output: {1: ['a'], 2: ['b'], 3: ['c']}

# Finding common key-value pairs
print("\nCommon key-value pairs in dictionaries:")
common_key_value_result = common_key_value_pairs(dict1, dict2, dict3)
print(common_key_value_result)  # Output: {}
