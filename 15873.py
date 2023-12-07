num = str(input())
sum = 0
for i in range(len(num)):
    sum = sum + int(num[i])

    if int(num[i]) == 0:
        sum += 9

print(sum)