import sys
N = int(sys.stdin.readline())

number = []
for i in range(N):
    num = int(sys.stdin.readline())
    number.append(num)

number.sort()

print(round(sum(number) / N))
print(number[N//2])

count = []
for i in range(-4000, 4001):
    count.append([i, 0])
# num을 돌면서 해당 숫자를 표현하는 인덱스번호에 1을 추가해준다
for num in number:
    count[num + 4000][1] += 1
# 갯수 기준으로 정렬
count.sort(key = lambda x: (-x[1], x[0]))
# 출력
if N == 1:
    print(number[0])
else:
    if count[0][1] != count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])

print(max(number) - min(number))