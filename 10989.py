import sys

N = int(sys.stdin.readline())

ans = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    ans[num] = ans[num]+1

for j in range(len(ans)):
    if ans[j] != 0:               # ans[j]번째가 0이 아니라면
        for k in range(ans[j]):   # ans[j]의 크키만큼
            print(j)              # j를 반복한다