import sys
import math

M, N = map(int, sys.stdin.readline().split())
ans = []

def check(num):
    if num  == 1 :
        return False
    for i in range(2, int(math.sqrt(num)) +1):
        if num % i ==0:
            return False
    return True

for i in range(M, N+1):
    if check(i):
        print(i)
