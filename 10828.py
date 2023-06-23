import sys

N = int(sys.stdin.readline())

ans =[]
for i in range(0,N):
    order = list(map(str, sys.stdin.readline().split()))
    
    if order[0] == "push":
        ans.append(order[1])
    elif order[0] == "pop":
        if not ans : # 빈리스트라면
            print(-1)
        else:
            print(ans[-1])
            ans.pop()
    elif order[0] == "size":
        if not ans :
            print(0)
        else:
            print(len(ans))
    elif order[0] == "empty":
        if not ans :
            print(1)
        else:
            print(0)
    else: # top
        if not ans : # 빈리스트라면
            print(-1)
        else:
            print(ans[-1])