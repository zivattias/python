# flag = True

# num = input("Enter a number to your list, $ to finish: ")
#
# while flag:
#     if not num.isdigit():
#         if num == '$':
#             flag = False
#         elif num[0] == '-':
#             if num[0::].isdigit():
#                 num_list.append(num)
#             else: print('Wrong input. Use numbers.')
#     else: num_list.append(num)
#
# print(num_list)
# num_list = [1, 2, 3, 4, 5]
# total_sum = 0
#
#
# def sums(l1):
#     _total_sum = 0
#     for i in l1:
#         _total_sum += i
#     return _total_sum
#
# total_sum = sums(num_list)
# print(total_sum)

def sum_list(nums_list: list) -> float:
    return sum(nums_list)


print(sum_list([4, 5, 6]))
