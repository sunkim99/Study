import sys

ans=[]
while(True):
    num = list(map(int, sys.stdin.readline().split()))
    num = sorted(num)
    a = num[0]
    b = num[1]
    c = num[2]    
    
    if a == 0 and b == 0 and c == 0 :
        for i in ans:
            print(i)
        break
    else:
        if (a**2 + b**2) == c**2 :
            ans.append("right")
        else:
            ans.append("wrong")

