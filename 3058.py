T = int(input())
for i in range(T):
    even_num = []
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            even_num.append(i)
    print(sum(even_num), min(even_num))