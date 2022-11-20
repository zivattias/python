# Function to determine last digit in ID number
def last_id_digit(id_num: str) -> str:
    # Digits strength assorted in a list
    num_strength: list = [1, 2, 1, 2, 1, 2, 1, 2]
    # ID number digits multiplied by strength, in a list
    num_multi: list = []
    # Digit sums for two-digit numbers
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
    full_id = "Your full ID number is: " + str(id_num) + str(last_digit)
    return full_id

# The application:
# Shows the instructions on how to use it.
# The application will randomly fit the remaining numbers
# 0 digits entered ⇒ application will generate all numbers
# 1-8 digits entered by user ⇒ application will generate the remaining digits
# More than 8 digits entered ⇒ application will reference only first 8

# Program greeting message:
print("Welcome to Ziv's ID generator. The program will generate a valid ID number according to your input.\n"
      "If can enter how many digits you want, ranging from 0 to 8 digits.\n"
      "Regardless of how many digits you entered - the program will complete the sequence to match valid Israeli ID.\n"
      "Let's start!")
# Initial user input:
app_id: str = input('Enter your input: ')
how_many_digits: int = len(app_id)


if __name__ == '__main__':
    print(last_id_digit(input('Enter your ID number without last digit: ')))
