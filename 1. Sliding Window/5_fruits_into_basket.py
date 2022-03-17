# Problem Statement
# Given an array of characters where each character represents a fruit tree, you are given two baskets 
# and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# Solution: This question is similar to longest_substring_with_k_distinct_characters. Here k = 2.

def fruits_into_basket(fruits):
    start, length = 0, 0
    fruit_frequency = {}
    for end in range(len(fruits)):
        if(fruits[end] not in fruit_frequency):
            fruit_frequency[fruits[end]] = 0
        fruit_frequency[fruits[end]] += 1

        while(len(fruit_frequency) > 2):
            fruit_frequency[fruits[start]] -= 1
            if(fruit_frequency[fruits[start]] == 0):
                del fruit_frequency[fruits[start]]
            start += 1
        length = max(length, end-start+1)
    return length


def main():
    print(fruits_into_basket(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']))


main()
