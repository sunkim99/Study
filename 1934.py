import sys


def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a


T = int(sys.stdin.readline())
ans=[0]*T
for i in range(0,T):
    A, B = map(int, sys.stdin.readline().split())
    ans[i] = int(A*B / gcd(A,B))

# 시간초과
# ans = [0] * T
# for i in range(0,T):
#     A, B = map(int, sys.stdin.readline().split())
#     for j in range(max(A,B) ,(A*B)+1):
#         if j % A == 0 and j % B == 0:
#             ans[i] = j
#             break


for k in ans:
    print(k)
