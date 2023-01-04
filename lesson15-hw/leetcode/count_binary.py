# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
# Input: s = "00110011"
# Output: 6

def count_binary(string: str):
    s_lens = list(map(len, string.replace('01', '0 1').replace('10', '1 0').split()))
    return sum(min(a, b) for a, b in zip(s_lens, s_lens[1:]))


s = '0011001'
print(count_binary(s))
