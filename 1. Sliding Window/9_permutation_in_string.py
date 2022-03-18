# Permutation in a String (hard)
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string.
# For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

# def are_sets_equal(freq1, freq2):
#     for i in range(26):
#         if freq1[i] != freq2[i]:
#             return False
#     return True


# def permutation_in_string(str, pattern):
#     if len(pattern) > len(str):
#         return False
#     freq1 = [0] * 26
#     freq2 = [0] * 26
#     for char in pattern:
#         freq2[ord(char)-ord('a')] += 1
#     start, end = 0, 0
#     while end < len(str):
#         freq1[ord(str[end])-ord('a')] += 1
#         if end-start + 1 == len(pattern):
#             # Alternatively we can use freq1 == freq2:
#             if are_sets_equal(freq1, freq2):
#                 return True
#         if end-start + 1 < len(pattern):
#             end += 1
#         else:
#             freq1[ord(str[start])-ord('a')] -= 1
#             start += 1
#             end += 1
#     return False


# def main():
#     print(str(permutation_in_string("odicf", "dc")))
#     print(str(permutation_in_string("aaacb", "abc")))


# main()


# SETTER'S Solution

# Create a HashMap of pattern string chars and take a int var matched. Keep on matching the char and if window size > pattern length
# then reduce window size.

def permutation_in_string(str, pattern):
    start, matched = 0, 0
    char_frequency = {}
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for end in range(len(str)):
        if str[end] in char_frequency:
            char_frequency[str[end]] -= 1
            # Freq became 0 hence the char got matched.
            if char_frequency[str[end]] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # If end-start+1 == len(pattern) then keep on sliding the window. Hence the condition end >= len(pattern)
        if end >= len(pattern)-1:
            # If the char got matched but we have to reduce window size.
            if str[start] in char_frequency:
                if char_frequency[str[start]] == 0:
                    matched -= 1
                char_frequency[str[start]] += 1
            start += 1

    return False


def main():
    print(str(permutation_in_string("odicf", "dc")))
    print(str(permutation_in_string("aaacb", "abc")))


main()
