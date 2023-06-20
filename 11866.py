import sys

N, K = map(int, sys.stdin.readline().split())
N_list =[]
for i in range(1,N+1):
    N_list.append(i)

ans = []
cnt = 0

for j in range(N):
    cnt += K-1
    cnt %= len(N_list)
    ans.append(N_list.pop(cnt))


print(f"<{', '.join(map(str, ans))}>")