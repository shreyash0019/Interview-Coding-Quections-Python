# Write a Python function to find the common elements in two lists.
def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example usage
print(find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))  # Output: [4, 5]
