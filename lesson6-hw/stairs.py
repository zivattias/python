# You are climbing a staircase. It takes n steps to reach the top.
#rs
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# n = 1; 1
# n = 2; 2
# n = 3; 3
# n = 4; 5

def stair_climb_options() -> int:
    ways: list = [1, 2]
    while True:
        num = input('Enter number of stairs to climb: ')
        if not num.isdigit():
            print('Use numbers only.')
        else:
            num = int(num)
            break
    if num == 1:
        return ways[0]
    elif num == 2:
        return ways[1]
    else:
        ways.append(num - 1 + num - 2)
        return ways[-1]

print(f"Unique ways to climb: {stair_climb_options()}.")
