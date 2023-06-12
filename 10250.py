import sys


T = int(sys.stdin.readline())
ans = []
for t in range(0,T):
    H, W, N = map(int, sys.stdin.readline().split())

    for i in range(1,W+1):
        for j in range(1,H+1):
            N -=1
            if N==0:
                if i <10:
                    room = str(0) + str(i)
                    ans.append(str(j)+room)
                else:
                    room= str(i)
                    ans.append(str(j)+room)

for k in ans:
    print(k)
