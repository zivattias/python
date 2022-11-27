# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Input: a = [1,2,3,0,0,0], m = 3, b = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,*2*,3,*5*,*6*] with the underlined elements coming from nums1.

def merge_sorted_array(a: list[int], m: int, b: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    k = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if a[p1] > b[p2]:
            a[k] = a[p1]
            p1 -= 1
        else:
            a[k] = b[p2]
            p2 -= 1
        k -= 1

    if p2 >= 0:
        a[:k + 1] = b[:p2 + 1]

nums1: list = [1, 2, 3, 0, 0, 0]
m: int = 3
nums2: list = [2, 5, 6]
n: int = 3

nums_1: list = [0]
m_2: int = 0
nums_2 = [1]
n_2 = 1

print(nums1)
merge_sorted_array(nums1, m, nums2, n)
print(nums1)
print(nums_1)
merge_sorted_array(nums_1, m_2, nums_2, n_2)
print(nums_1)


# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.