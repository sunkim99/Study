ans =[]
for i in range(1,10):
    ans.append(int(input()))

print(max(ans))
print(ans.index(max(ans))+1)