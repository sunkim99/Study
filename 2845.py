import sys

L, P = map(int, sys.stdin.readline().split())

candidate = list(map(int, sys.stdin.readline().split()))

ans = []

for i in candidate:
    ans.append(i-(L*P))

print(' '.join(map(str, ans)))
