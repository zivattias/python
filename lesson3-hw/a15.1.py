fibo = [0, 1]
for x in range(9):
    fibo.append(fibo[x] + fibo[x+1])
print(fibo)
