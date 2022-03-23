# PATTERN TWO POINTERS

# In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements
# that fulfill certain constraints, the Two Pointers approach becomes quite useful.
# The set of elements could be a pair, a triplet or even a subarray.

# For example, take a look at the following problem:
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

def pair_target_sum(array, target):
    front, back = 0, len(array)-1
    while front < back:
        if array[front]+array[back] < target:
            front += 1
        elif array[front]+array[back] > target:
            back -= 1
        else:
            return [array[front], array[back]]
    return -1


def main():
    array = [1,2,3,4,5,6]
    target = 6
    if pair_target_sum(array, target) == -1:
        print("Array doesn't contain any pair with sum equal to target.")
    else:
        print(pair_target_sum(array, target))


main()
