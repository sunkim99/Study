import sys

k = int(sys.stdin.readline())

num =[]
for i in range(0,k):
    n = int(sys.stdin.readline())
    if n ==0:
        num.pop()
    else:
        num.append(n)

print(sum(num))