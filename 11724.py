import sys


sys.setrecursionlimit(10 ** 6)
# python은 재귀호출 횟수가 1,000회로 제한되어있어서 제한을 늘려준다

N , M = map(int ,sys.stdin.readline().split())
uv = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    uv[u][v] = True
    uv[v][u] = True

ans = 0
chk = [False] * (N+1)

def dfs(i):
    for j in range(1, N+1):
        if uv[i][j] and not chk[j]:
            chk[j] = True
            dfs(j)

for i in range(1, N+1):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)

'''
무방향 그래프 = 양방향 그래프
a->b , b->a 가 가능하다

'''