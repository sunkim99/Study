import sys

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N,B = map(int, sys.stdin.readline().split())
ans = ''

while N != 0 :
    ans += str(tmp[N%B])
    N = N // B

print(ans[::-1])