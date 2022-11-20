id_num: str = '04798562'
num_list: list = []  # [0, 4, 7, 9, 8, 5, 6, 2]
num_strength: list = [1, 2, 1, 2, 1, 2, 1, 2]
num_multi: list = []  # [0, 8, 7, 18, 8, 10, 6, 4]
num_sum: list = []  # [0, 8, 7, 1+8, 8, 1+0, 6, 4]

for i in range(len(id_num)):
    num_list.append(int(id_num[i]))

for j in range(len(num_list)):
    num_multi.append(num_strength[j] * num_list[j])

for k in range(len(num_multi)):
    if num_multi[k] >= 10:
        num_sum.append(int(str(num_multi)[k][0]) + int(str(num_multi)[k][1]))
    else:
        num_sum.append(num_multi[k])


print(num_list)
print(num_multi)

# def id_verification(num: str) -> int:
#     num_list.append(num.split(''))
#     for i in num_list:
#         nums_sum.append(num_list[i])
#         for idx, figure in enumerate(nums_sum):
#
