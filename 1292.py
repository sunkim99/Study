A,B = map(int, input().split())
num =[]
for i in range(1, 100):
    for j in range(i):
        num.append(i)

print(sum(num[A-1:B]))