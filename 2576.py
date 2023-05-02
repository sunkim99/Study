num = 0
numli = []
li = [int(input()) for _ in range(0,7)]
for i in range(len(li)):
    if li[i] % 2 == 1 :
        num += li[i]
        numli.append(li[i])


if num ==0:
    print(-1)
else :
    print(num)
    print(min(numli))