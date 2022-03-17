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

def are_sets_equal(freq1, freq2):
    for i in range(26):
        if freq1[i] != freq2[i]:
            return False
    return True


def permutation_in_string(str, pattern):
    if len(pattern) > len(str):
        return False
    freq1 = [0] * 26
    freq2 = [0] * 26
    for char in pattern:
        freq2[ord(char)-ord('a')] += 1
    start, end = 0, 0
    while end < len(str):
        freq1[ord(str[end])-ord('a')] += 1
        if end-start + 1 == len(pattern):
            # Alternatively we can use freq1 == freq2:
            if are_sets_equal(freq1, freq2):
                return True
        if end-start + 1 < len(pattern):
            end += 1
        else:
            freq1[ord(str[start])-ord('a')] -= 1
            start += 1
            end += 1
    return False


def main():
    print(str(permutation_in_string("odicf", "dc")))
    print(str(permutation_in_string("aaacb", "abc")))


main()
