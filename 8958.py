case = int(input())
answer=[]
for i in range(0,case):
    score =0
    result = str(input())
    pre =0 
    for j in range(0,len(result)):
        if result[j] == "O":
            if j ==0: # 첫번째가 O일때
                score += 1
                pre +=1
            else: # 첫번째가 아닐때
                if result[j-1] == "O":
                    pre = pre+ 1
                    score += pre
                else :
                    score += 1
                    pre = 1
        else:
            pass
    answer.append(score)

for k in answer:
    print(k)