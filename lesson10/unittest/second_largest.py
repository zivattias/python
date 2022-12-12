def second_largest(nums: list[float]) -> float | None:
    """
    We want to return None if there is no second-max number.
    For example, if there are less than 2 numbers in the list,
    or if all the numbers are equal
    :param nums:
    :return: second-largest number
    """

    # if there are less than 2 elements - there is no second largest
    if len(nums) in (0, 1):
        return None

    max_num, second_max = None, None

    for n in nums:
        if max_num is None:
            max_num = n
        else:
            if n > max_num:
                second_max = max_num
                max_num = n
            else:
                if second_max is None:
                    if n != max_num:
                        second_max = n
                else:
                    if second_max < n < max_num:
                        second_max = n

    return second_max


if __name__ == '__main__':
    test_lists = (
        [3, -4, 2, 3, 0],
        [0, 3, 0],
        [3, 0, 3],
        [3, 3, 3, 3],
        [0, -3, -3, -2, -10],
        [-9, -5, -3, -5, -1],
        [3, 6, 9, 4, 5]
    )
    for nums in test_lists:
        print(f"The second largest of {nums} is {second_largest(nums)}")