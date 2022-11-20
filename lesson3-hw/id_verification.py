def last_id_digit(id_num: str) -> str:
    num_strength: list = [1, 2, 1, 2, 1, 2, 1, 2]
    num_multi: list = []
    num_sum_list: list = []
    for i in range(len(id_num)):
        num_multi.append(num_strength[i] * int(id_num[i]))
        if num_multi[i] >= 10:
            num_sum_list.append(num_multi[i] % 10 + num_multi[i] // 10)
        else:
            num_sum_list.append(num_multi[i])
    digits_sum: int = sum(num_sum_list)
    if digits_sum % 10 != 0:
        last_digit: int = 10 - (digits_sum % 10)
    else:
        last_digit = 0
    full_id = str(id_num) + str(last_digit)
    return full_id

if __name__ == '__main__':
    print(last_id_digit(input('Enter your ID number without last digit: ')))
