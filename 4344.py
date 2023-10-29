c= int(input())

for i in range(c):
    avg_list = list(map(int, input().split()))

    avg = sum(avg_list[1:]) / avg_list[0]
    cnt =0
    for j in avg_list[1:]:
        if j > avg:
            cnt+=1

    per = (cnt / avg_list[0]) *100
    print(f'{per:.3f}%')