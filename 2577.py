A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
ans =[]
for i in range(0,10):
    num = 0
    for j in str(mul):
        if int(j) == i :
            num +=1 
        else:
            pass
    ans.append(num)

for k in ans:
    print(k)