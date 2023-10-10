import sys

A,B = map(int, sys.stdin.readline().split())
price = int(sys.stdin.readline())

ch = price*2
if ch > (A+B):
    print(A+B)
else:
    print((A+B) - ch)