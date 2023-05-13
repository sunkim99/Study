N = int(input())
num = map(int, input().split())
answer=0

for i in num:
    err =0
    if i > 1:
        for j in range(2,i):
            if i % j == 0 :
                err += 1
                # 2부터 i-1까지 나눈 몫이 0이면 값 증가
        if err ==0:
            answer += 1
            # 증가된 값이 없으면 소수, answer에 값 증가

print(answer)