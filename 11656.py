S = input()

ans = []
for i in range(len(S)):
    ans.append(S[i:])
    
for j in sorted(ans):
    print(j)