from collections import deque
import sys

T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    que = deque(list(map(int, sys.stdin.readline().split())))
    cnt =0
    while que:
        best = max(que)
        front = que.popleft()
        M -= 1

        if best == front :
            cnt += 1
            if M < 0 :
                print(cnt)
                break
        else:
            que.append(front)
            if M < 0:
                M = len(que) - 1