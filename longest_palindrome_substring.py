# Question: Write a Python function to find the longest palindromic substring in a given string.
def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    longest = s[0]
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest
