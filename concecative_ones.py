# Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1s that can be achieved.
def longest_ones(string):
    ans = 0
    n = len(string)
    left_ones = [0]*n  # List to store number of consecutive ones on the left of ith index till ith index 
    right_ones = [0]*n  # List to store number of consecutive ones on the right of ith index till ith index 
    total_ones = 0  # Total number of ones in the string
    for i in range(n):
        if string[i] == '1':
            total_ones += 1
    left_ones[0] = int(string[0])    
    for i in range(1, n):  # Loop to generate left_ones array
        if string[i] == '1':
            left_ones[i] = left_ones[i-1]+1
        else:
            left_ones[i] = 0
    right_ones[n-1] = int(string[n-1])
    for i in range(n-2, -1, -1):  # Loop to generate right_ones array
        if string[i] == '1':
            right_ones[i] = right_ones[i+1]+1
        else:
            right_ones[i] = 0

    if len(string) == total_ones:  # To handle all 1s in a string
        return total_ones    
    for i in range(n):
        if string[i] == '0':
            if i == 0:  # To handle first character
                if right_ones[i+1]+1 < total_ones:
                    ans = max(ans, right_ones[i+1]+1)
                else:
                    ans = max(ans, right_ones[i+1])
            elif i == n-1:  # To handle last character
                if left_ones[i-1]+1 < total_ones:
                    ans = max(ans, left_ones[i-1]+1)
                else:
                    ans = max(ans, left_ones[i-1])
            else:
                if left_ones[i-1]+right_ones[i+1]+1 < total_ones:
                    ans = max(ans, left_ones[i-1]+right_ones[i+1]+1)
                else:
                    ans = max(ans, left_ones[i-1]+right_ones[i+1])
    return ans
