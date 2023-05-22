N = int(input())
ans =[]
for i in range(0,N):
    R, S = map(str, input().split())
    R = int(R)
    word = ''
    for j in range(len(S)):
        word += S[j]*R
    ans.append(word)
        

for k in ans:
    print(k)
