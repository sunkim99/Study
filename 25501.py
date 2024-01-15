import sys
input = sys.stdin.readline # 입력 시간초과를 방지하기 위해 input을 sys함수로 대체

def recursion(s, l, r):
    global cnt # 전역변수 : 함수 밖에서도 사용가능
    cnt += 1 # 함수가 호출 될 때마다 +1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())

for _ in range(N):
    cnt = 0 # 하나씩 확인 할 때마다 0으로 초기화
    print(isPalindrome(input().rstrip()), cnt) # .rstrip()을 사용해서 sys함수의 줄바꿈을 삭제