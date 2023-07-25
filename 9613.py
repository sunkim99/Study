from math import gcd
import sys


'''
GCD = 최대 공약수
'''
t = int(sys.stdin.readline())

ans = [] 
for i in range(0,t):
    num = list(map(int, sys.stdin.readline().split()))
    n = num[0]
    num.pop(0)
    total = 0
    for j in range(0,n):
        for k in range(j+1, n): 
            total += gcd(num[j], num[k])
    ans.append(total)
    
for j in ans:
    print(j)