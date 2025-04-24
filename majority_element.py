# Question: Write a Python function to find the majority element (an element that appears more than n/2 times) in an array.
def majority_element(nums):
    from collections import Counter
    count = Counter(nums)
    for key, value in count.items():
        if value > len(nums) // 2:
            return key
    return None
