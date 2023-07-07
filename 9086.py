T = int(input())
ans =[]
for i in range(0,T):
    word= str(input())

    ans.append(word[0]+word[-1])

for j in ans:
    print(j)