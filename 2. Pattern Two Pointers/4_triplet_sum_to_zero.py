# TRIPLET SUM TO ZERO

# Problem Statement
# Given an arraay of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def triplet_sum_zero(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        curr = nums[i]
        left = i+1
        right = len(nums)-1
        while left < right:
            sum = curr + nums[left] + nums[right]
            if sum == 0:
                ans.append([curr, nums[left], nums[right]])
                left += 1
                right -= 1
                while (left < right and nums[left] == nums[left-1]):
                    left += 1
                while (left < right and nums[right] == nums[right+1]):
                    right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return ans


def main():
    print(triplet_sum_zero([-5, 2, -1, -2, 3]))
    print(triplet_sum_zero([-3, 0, 1, 2, -1, 1, -2]))


main()
