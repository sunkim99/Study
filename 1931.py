import sys

N = int(sys.stdin.readline())
ans =[]
for i in range(0,N) :
    start, end = map(int, sys.stdin.readline().split())
    ans.append((end, start)) # 끝나는 시간을 먼저 넣는다

ans.sort() # 0번 인덱스에 대해서 정렬, 같은 0번일경우 1번인덱스도 정렬

time = 0
num = 0

for end, start in ans:
    if time <= start :
        num += 1
        time = end

print(num)