import sys
from bisect import bisect_left, bisect_right


M = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))

M2 = int(sys.stdin.readline())
num_2 = list(map(int, sys.stdin.readline().split()))

ans = [0] * M2
for i in range(0,M2):
    a = bisect_left(num,num_2[i])
    b = bisect_right(num,num_2[i])
    if abs(a-b) != 0:
        ans[i] = 1

for j in ans:
    print(j)
