# Longest Substring with Same Letters after Replacement (hard)

# Problem Statement
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

# BRUTE FORCE

# def length_of_longest_substring(str, k):
#     max_length = 0
#     for i in range(len(str)):
#         temp_k = k
#         for j in range(i, len(str)):
#             if(str[j] != str[i]):
#                 temp_k -= 1
#             if temp_k < 0:
#                 break
#             max_length = max(max_length, j-i+1)
#     return max_length


# def main():
#     print(length_of_longest_substring("aabccbb", 2))
#     print(length_of_longest_substring("abbcb", 1))

# main()

# OPTIMIZED

def length_of_longest_substring(str, k):
    max_length, max_repeating_char_count = 0, 0
    start = 0
    char_frequency = {}
    for end in range(len(str)):
        # If element is not in HashMap then putting it and if it is then increasing its frequency.
        if str[end] not in char_frequency:
            char_frequency[str[end]] = 0
        char_frequency[str[end]] += 1

        # Changing the max repeating chars count in the current window.
        max_repeating_char_count = max(
            max_repeating_char_count, char_frequency[str[end]])

        # If the current window has more than k chars other than max repeating char then it's time to
        # to shrink the window.
        # Increase the start and decrease the element left's frequency.
        
        if(end - start + 1 - max_repeating_char_count > k):
            char_frequency[str[start]] -= 1
            if(char_frequency[str[start]] == 0):
                del char_frequency[str[start]]
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))


main()