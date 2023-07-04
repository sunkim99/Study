import sys

N, L = map(int, sys.stdin.readline().split())
coord = [False] * 1001

for i in map(int, sys.stdin.readline().split()):
    coord[i] =True

ans = 0
x = 0
while x <= 1000:
    if coord[x] :
        ans += 1
        x += L
    else:
        x += 1

print(ans)