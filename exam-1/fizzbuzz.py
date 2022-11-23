# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# ret_val[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ret_val[i] == "Fizz" if i is divisible by 3.
# ret_val[i] == "Buzz" if i is divisible by 5.
# ret_val[i] == i (as a string) if none of the above conditions are true.

def fizzbuzz(n: int) -> list[int]:
    _l = list()
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            _l.append('FizzBuzz')
        elif i % 3 == 0:
            _l.append('Fizz')
        elif i % 5 == 0:
            _l.append('Buzz')
        else:
            _l.append(i)
    return _l

while True:
    num = input('Enter number of values: ')
    if not num.isdigit():
        print(f'You entered {num}. Use numbers please.')
    else:
        num = int(num)
        print(fizzbuzz(num))
        break



