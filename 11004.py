import sys

N, K = map(int, sys.stdin.readline().split())

ans = sorted(list(map(int, sys.stdin.readline().split())))

print(ans[K-1])