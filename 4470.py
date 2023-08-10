N = int(input())
ans =[]
for i in range(0,N):
    ans.append(input())

for j in range(len(ans)):
    print('{0}. {1}'.format(j+1, ans[j]))