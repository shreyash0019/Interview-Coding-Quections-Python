# Write a Python function to check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
