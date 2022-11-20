# First option:
year = int(input("Your birth year: "))
age = 2022 - year
print("Your are", age, "years old")

# Second option (less common):
print("You are", 2022 - int(input("Your birth year: ")), "years old")

# A1
height = int(input("Please enter the rectangle's height: "))
width = int(input("Please enter the rectangle's width: "))
per = 2 * (height + width)
area = height * width
print(f"According to set height and width, the area is {area}. The perimeter is {per}.")

# A2
temp_c = int(input("Please enter the temp in Celsius: "))
temp_f = (temp_c * 1.8) + 32
print("Temp in Fahrenheit:", temp_f)

# A8
salary = int(input("Hi Bob, please enter your salary: "))
donation = salary * 0.14
print("Your donation amount (%14) is: $" + str(donation))

my_text = "January" \
    "February" \
    "March"

my_text = "January\n" \
    "February\n" \
    "March"

my_text = """January
February
March"""

# String & Index examples:
print(my_text)  # Print entire string
print(my_text[5])   # Print the sixth letter in the string, index 5
print(my_text[5:8])  # Print the sixth & seventh letters in the string, index 5-8
print(my_text[5:])  # Print the fifth letter and the rest in the string
print(my_text[:5])  # Print until the fifth letter
print(my_text[-1])  # Print the last letter in the string, one index backward from index '0' (first letter)
print(my_text[-1:-5])   # Invalid print!
print(my_text[-5:-1])   # Print from the fifth letter to the end, until the first
print(my_text[2:10:2])  # Print from index 2 to 10 (not including), by jumps of 2
print(my_text[10:2:-1])  # Print from letter in index 10 until letter index 2, in reverse (-1)
print(my_text[::-1])    # Print the whole string in reverse

drink = input("What did you drink tonight? ")  # beer / wine
qty = float(input("How much did you drink of that? "))
can_drive = (drink == 'beer' and (qty <= 0.3)) or \
            (drink == 'wine' and qty <= 0.2)
print("Can drive:", can_drive)
