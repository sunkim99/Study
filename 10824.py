import sys

A,B,C,D = map(str, sys.stdin.readline().split())


ab = A+B
cd = C+D
print(int(ab) + int(cd))