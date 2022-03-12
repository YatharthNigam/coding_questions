# Problem Statement
# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def non_repeat_substring(string):
    char_last_index = {}
    start, length = 0, 0
    for end in range(len(string)):
        if string[end] not in char_last_index:
            char_last_index[string[end]] = end
        else:
            start = max(start, char_last_index[string[end]]+1)
        length = max(length, end - start + 1)
    return length


def main():
    length = non_repeat_substring("aabccbb")
    print(length)


main()

# Storing the last index of repeating character and making start as last index + 1
