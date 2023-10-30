import sys

def factorial(num):
    n = 1
    for i in range(1,num+1):
        n *= i
    return n


T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    bridge = factorial(M) // (factorial(N) * factorial(M-N))
    # mCn (조합) -> (M-N)! * N! 을 M!으로 나눈다
    print(bridge) 
