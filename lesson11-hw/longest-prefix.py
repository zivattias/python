# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def longest_prefix(strs: list[str]):
    p = ""
    if not strs:
        return p
    if len(strs) == 1:
        return strs[0]

    strs.sort()

    for letter_1, letter_2 in zip(strs[0], strs[-1]):
        if letter_1 == letter_2:
            p += letter_1
        else:
            break

    return p

print(longest_prefix(['flower', 'flow', 'flight', 'flamingo']))
print(longest_prefix(["dog","racecar","car"]))
print(longest_prefix(['baremingspg', 'bareasklfjkla', 'baremakslfjkies', 'bareyoijio']))