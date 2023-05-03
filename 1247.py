import sys


for i in range(3):
    n_sum =0
    for i in range(0,int(sys.stdin.readline())):
        # num = input()
        n_sum += int(sys.stdin.readline())

    if n_sum == 0:
        print(0)
    elif n_sum > 0:
        print("+")
    else :
        print("-")

'''
input()은 
    1. 입력을 받고 
    2. 문자열로 변환하고
    3. 추가 strip을 진행
하는과정을 거친다.
그리고 사용자로부터 입력을 받기 전 대기를 위한 prompt를 가지고있다
때문에 많은 여러줄의 입력을 받는 경우,
한줄 입력 받기 -> 단계 수행 -> 대기(prompt)를 반복한다고한다.

그래서 시간이 오래걸려서 자꾸 시간초과가 발생했던것.

이에 사용하는게 sys.stdin.readline()이라고한다.

+ input()은 더이상 입력이 없는데도 수행될경우 런타임 에러 (EOFError)를 뱉어낸다고..
sys.stdin.readline()은 빈 문자열을 반환한다고한다.
    
'''
