import sys

n,m = map(int, sys.stdin.readline().split())

print(int(n//m))
print(int(n%m))