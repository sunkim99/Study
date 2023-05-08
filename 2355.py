import sys

a,b = map(int, sys.stdin.readline().split())

# 2S = (n+m) * (m-n+1) 가우스 공식
if a < b :
    print((a + b) * (b - a + 1 ) // 2)

else:
    print((a + b) * (a - b + 1 ) // 2)