N = int(input())
data =[]
ans =[]

for i in range(N):
    x,y = map(int, input().split())
    data.append((x,y))

for i in range(N):
    cnt = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt +=1
    ans.append((cnt + 1))

for i in ans:
    print(i)