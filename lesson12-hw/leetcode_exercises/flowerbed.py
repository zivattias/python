# You have a long flowerbed in which some pots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

def can_plant(bed: list[0 | 1], n: int) -> bool:
    count = 0
    flowerbed = [0] + bed + [0]

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1

    return count >= n


print(can_plant([0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1], 4))
print(can_plant([0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1], 3))
