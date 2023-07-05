import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

ans = []
num = list(map(int, sys.stdin.readline().split()))

for i in combinations(num, 3):
    if sum(i) <= M:
        ans.append(i)

new =[]
for j in ans:
    new.append(sum(j))

print(max(new))