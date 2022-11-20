# data = [0, 1]
#
# for x in data:
#     for y in data:
#         print(x, y)

nums: list = [6, 2, 4, 3]
target: int = 7
output: list = []

# complexity n^2
for i in nums:
    if len(output) == 2:
        break
    for j in nums:
        if i + j == target:
            output.append(nums.index(i))
            output.append(nums.index(j))
print(output)

# complexity < n^2
