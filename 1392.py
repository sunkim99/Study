import sys
N, Q = map(int, sys.stdin.readline().split())

music = [int(sys.stdin.readline()) for _ in range(N)]
q = [int(sys.stdin.readline()) for _ in range(Q)]

result = []

i = 1
for j in music:
    # 예를 들어서 1번 악보가 2초이면 두번 띄워줍니다. ex: 1, 1, 2, 3, 3, 3 
    for _ in range(j):
         # 1, 1, 2, 3, 3, 3
        result.append(i)
    i = i + 1

for k in q:
    # k가 2이면 result의 두번째 인덱스는 2이다.
    print(result[k])