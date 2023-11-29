import sys

N = int(input())
for i in range(N):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print("even")
    else:
        print("odd")