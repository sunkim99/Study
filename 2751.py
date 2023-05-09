import sys

N = int(sys.stdin.readline())
answer =[]
for i in range(0,N):
    answer.append(int(sys.stdin.readline()))

for j in sorted(answer):
    print(j)