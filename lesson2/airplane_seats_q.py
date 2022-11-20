# ABC DEF -> 3 3
# AB CDE FG -> 2 3 2

layout = input("Enter the seats layout: ")
seat = layout.split(" ")
print(f"Given seat structure: {seat}")
# for one batch:
if len(seat) == 1:
    print(len(seat[0]))
# for two:
if len(seat) == 2:
    print(len(seat[0]), len(seat[1]))
# for three:
if len(seat) == 3:
    print(len(seat[0]), len(seat[1]), len(seat[2]))

# Another solution:
seats = input("Enter seats formation: ")
groups = seats.split(' ')

if len(groups) > 1:
    g1 = str(len(groups[0]))
    g2 = str(len(groups[1]))
    if len(groups) > 2:
        g3 = str(len(groups[2]))
        print(g1, g2, g3)
    else:
        print(g1, g2)
else:
    print(len(groups[0]))
