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
    sum,temp = 0,0
    window_start = 0
    for window_end in range(len(array)):
        temp += array[window_end]
        if window_end >= k-1:
            sum = max(sum,temp)
            temp -= array[window_start]
            window_start += 1
    return sum

def main():
    sum  = max_subarray_size_k([2,1,5,1,3,2], 3)
    print(sum)

main()