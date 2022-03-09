# Problem Statement
# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import math


def smallest_subarray_with_given_sum(s, arr):
    sum, start = 0, 0
    len = math.inf
    for end in range(0, len(arr)):
        sum += arr[end]
        while sum >= s:
            len = min(end - start+1, len)
            sum -= arr[start]
            start += 1
    if sum == math.inf:
        return 0
    return len


def main():
    length = smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])
    print(length)


main()
