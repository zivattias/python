# complexity = n^2
nums: list = [6, 2, 4, 3]
target: int = 7
output: list = []

for i in nums:
    if len(output) == 2:
        break
    for j in nums:
        if i + j == target:
            output.append(nums.index(i))
            output.append(nums.index(j))
print(output)

# complexity < n^2
nums2: list = [6, 2, 4, 3]
target2: int = 7
indices: dict = {}

for i, num in enumerate(nums2):
    if target2 - num in indices:
        print([indices[target - num], i])
    else:
        indices[num] = i
