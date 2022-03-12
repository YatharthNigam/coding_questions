# Problem Statement
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct(str, k):
    char_frequency = {}
    max_length = 0
    start = 0
    for end in range(len(str)):
        right_char = str[end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the window, until we are left with 'k' characters
        while len(char_frequency) > k:
            char_frequency[str[start]] -= 1
            if(char_frequency[str[start]] == 0):
                del char_frequency[str[start]]
            start += 1

        # remember the max length
        max_length = max(max_length, end - start+1)
    return max_length


def main():
    print("Length of longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))


main()
