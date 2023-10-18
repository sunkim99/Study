num = int(input())

cnt = 0
new = num
while True:
    a = new // 10
    b = new % 10
    c = (a+b) % 10
    new = (b*10) + c
    cnt += 1

    if new == num:
        break

print(cnt)

# 10의 자리 수를 구하는 것은 10으로 나눈 몫, 
# 1의 자리 수를 구하는 것은 10으로 나눈 나머지를 활용하여 필요한 숫자를 만든다