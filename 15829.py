import sys

L = int(sys.stdin.readline())
word = str(sys.stdin.readline())

ans = 0
for i in range(0,L):
    ans += (ord(word[i]) -96) * (31 ** i)
print(ans % 1234567891)