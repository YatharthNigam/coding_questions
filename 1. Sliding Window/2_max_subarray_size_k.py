# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def max_subarray_size_k(array, k):
    max_sum, sum = 0, 0
    window_start = 0
    for window_end in range(len(array)):
        sum += array[window_end]
        # We don't need to increase when we hit the k. We have to increase by 1 each time after end > k-1
        if window_end >= k-1:
            max_sum = max(max_sum, sum)
            sum -= array[window_start]
            window_start += 1
    return max_sum


def main():
    max_sum = max_subarray_size_k([2, 1, 5, 1, 3, 2], 3)
    print(max_sum)


main()
