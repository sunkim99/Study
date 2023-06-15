import sys

N, K = map(int, sys.stdin.readline().split())

N_pac =1
for i in range(1,N+1):
    N_pac *= i

K_pac = 1
for j in range(1,K+1):
    K_pac *= j

NK_pac =1
for k in range(1,(N-K+1)):
    NK_pac *= k

print(int(N_pac / (K_pac * NK_pac)))