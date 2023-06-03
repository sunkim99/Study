import sys

n = int(sys.stdin.readline())
ans =[]
for i in range(0,n):
    A, B = map(int, sys.stdin.readline().split())
    ans.append(A+B)

for j in ans:
    print(j)