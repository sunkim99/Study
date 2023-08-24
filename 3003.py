c = list(map(int, input().split()))
c_list = [1,1,2,2,2,8]
ans=[]
for i in range(len(c_list)):
    ans.append(c_list[i] - c[i])

print(' '.join(map(str, ans)))