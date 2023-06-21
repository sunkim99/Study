import sys
# 시간초과에는 import sys 사용하기!


N = int(sys.stdin.readline())

ans =[]
for i in range(1,N+1):
    order = str(sys.stdin.readline())
    order_list = order.split()
    
    if order_list[0] == "push":
        ans.append(int(order_list[1]))
    elif order_list[0] =="pop":
        if not ans:
            print(-1)
        else:
            print(ans.pop(0))
    elif order_list[0] =="size":
        print(len(ans))
    elif order_list[0] =="empty":
        if not ans :
            print(1)
        else:
            print(0)
    elif order_list[0] =="front":
        if not ans :
            print(-1)
        else:
            print(ans[0])
    else: #back
        if not ans:
            print(-1)
        else:
            print(ans[-1])