N, X = map(int,input().split())

answer=[]
number = list(map(int, input().split()))


for j in number:
    if j < X:
        answer.append(j)
    else:
        pass

for i in answer:
    print(i , end=' ')