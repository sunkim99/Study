import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

stack = []

# 막대기 높이 입력받아 stack에 저장
for _ in range(n):
    h = int(input())
    stack.append(h)

cnt = 0 # 보이는 막대기의 개수를 카운트하기 위해 초기화
max_h = 0 # 현재 기준으로 가장 높은 막대기의 높이를 저장하기 위해 초기화

# 스택 오른쪽부터 왼쪽끝까지 탐색해서 보이는 막대기 개수 카운트
for i in range(n-1, -1, -1):
    if stack[i] > max_h:
        cnt += 1
        max_h = stack[i]

print(cnt) #보이는 막대기 출력