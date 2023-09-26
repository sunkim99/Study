import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
cost =[]
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    cost.append(a*b)

if sum(cost) == X :
    print("Yes")
else:
    print("No")