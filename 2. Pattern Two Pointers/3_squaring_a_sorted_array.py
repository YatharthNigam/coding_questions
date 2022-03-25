# SQUARING A SORTED ARRAY

# Problem Statement
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def squaring_sorted_array(arr):
    squares = [0 for i in range(len(arr))]
    left, right = 0, len(arr)-1
    highest_index = len(arr)-1
    while (left <= right):
        left_square = arr[left]**2
        right_square = arr[right]**2
        if (left_square < right_square):
            squares[highest_index] = right_square
            highest_index -= 1
            right -= 1
        else:
            squares[highest_index] = left_square
            highest_index -= 1
            left += 1
    return squares


def main():
    print(squaring_sorted_array([-3, -1, 0, 1, 2]))


main()

# Explanation: Take two pointers left and right and then fill the new array with one which is greater
# between them and the reduce left or increase right. Pretty easy question.
