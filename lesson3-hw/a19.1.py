#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n = int(input("Enter a number: "))

k = n - 1

# loop rows
for i in range(n):
    # for the spaces before *
    for j in range(k):
        print(end=" ")

    # update k to have one less space in the next iteration
    k -= 1

    # print the *
    for j in range(i + 1):
        print("* ", end="")
    print()