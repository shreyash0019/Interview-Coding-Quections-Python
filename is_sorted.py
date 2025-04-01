# Write a Python function to check if a list is sorted in ascending order.
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example usage
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False
