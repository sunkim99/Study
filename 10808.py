S = list(input())

ans =[]

for i in range(97,123):
    cnt =0
    for j in S:
        if ord(j) == i:
            cnt+=1

    ans.append(str(cnt))

print(' '.join(ans))