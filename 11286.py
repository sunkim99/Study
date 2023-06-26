import sys
import heapq

h = []
N = int(sys.stdin.readline())

for i in range(0,N):
    x = int(sys.stdin.readline())

    if x != 0:
        # x가 0이 아니라면 배열에 x값 넣기
        heapq.heappush(h, (abs(x), x))
        # 절댓값과 원본값을 튜플로 넣는다
    else:
        # x == 0
        # h가 비지 않았다면 h에 튜플로 들어가있으니 1번째를 출력한다
        # 비어있다면 0을 출력한다
        print(heapq.heappop(h)[1] if len(h) else 0) 
        