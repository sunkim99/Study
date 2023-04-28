
iou = ['a','e','i','o','u']
cnt =0
answer=[]
while(True):
    sen = input()
    if sen == "#":
        break
    for i in sen:
        if i.lower() in iou:
            cnt+=1
    answer.append(cnt)
    cnt=0

for i in answer:
    print(i)