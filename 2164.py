from collections import deque
import sys


N = int(sys.stdin.readline())
dq = deque()
for i in range(1,N+1):
    dq.append(i)

while len(dq) >1: 
    #제일 마지막에 남게되는 카드를 구하는거니까 len(dq)가 1개는 남아있어야
    dq.popleft() # 먼저들어온거부터 나가고
    dq.append(dq.popleft()) # 가장 안쪽(왼쪽)에있는 카드를 위로 올린다(=오른쪽으로 옮겨준다.)

print(dq[0])
