
ans =[]
for i in range(0,2):
    i, m, s, e = map(int, input().split())
    ans.append(i+m+s+e)

print(max(ans))