import sys
a,b = map(int,sys.stdin.readline().split())

ans =0
for i in range(min(a,b),0,-1):
    if a % i ==0 and b % i ==0:
        ans= i
        break

print(ans)
print(int((a*b) / ans))