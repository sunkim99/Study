T = int(input())

for i in range(T):
    number = sorted(list(map(int, input().split())))
    print(number[-3])
    