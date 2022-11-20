age = int(input("Enter your age: "))
height = int(input("Enter your height: "))

if age < 8:
    print("You're too young to ride the roller-coaster.")
elif (age <= 18 and height >= 115) or (age > 18 and height >= 100):
    print("Buckle up.")
else:
    print("Sorry, you're too short to ride.")