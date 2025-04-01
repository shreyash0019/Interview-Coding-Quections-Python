def find_second_largest(lst):
    first = second = float('-inf')
    for number in lst:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second

# Example usage
print(find_second_largest([1, 2, 3, 4, 5]))  # Output: 4
