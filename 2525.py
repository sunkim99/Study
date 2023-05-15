H, M = map(int,input().split())
time = int(input())

add_h, add_m = divmod(time,60)
M = M+add_m
H = H+add_h

if M >= 60 :
    min_h, min_m = divmod(M, 60)
    H += min_h  
    if H >=24:
        print(H-24 , min_m)
    else:
        print(H,min_m)
else:
    if H >=24:
        print(H-24, M)
    else:
        print(H,M)