# In many problems dealing with an array ( or a LinkedList),
# we are asked to find or calculate something among all the contiguous subarrays ( or sublists) of a given size.
# For example, Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# ---BRUTE FORCE---

# def find_averages_of_subarrays(K, arr):
#     result = []
#     for i in range(len(arr)-K+1):
#         sum = 0.0
#         for j in range(i,i+K):
#             sum += arr[j]
#         result.append(sum/K)
#     return result

# def main():
#     result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
#     print(result)

# main()

# ---OPTIMIZED---
# Not adding repeated elements and only adding one new element and subtracting previous element. SLIDING WINDOW

def find_averages_of_subarrays(K, arr):
    result = []
    window_start, sum = 0, 0.0
    start = 0
    for window_end in range(len(arr)):
        sum += arr[window_end]
        if window_end >= K-1:
            result.append(sum/K)
            sum -= arr[window_start]
            start += 1
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(result)


main()
