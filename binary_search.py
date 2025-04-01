# Write a Python function to implement binary search on a sorted list.
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # Output: -1
