import sys

N = int(sys.stdin.readline())
if N == 0:
    print(0)
else:
    pac = 1
    for i in range(1,N+1):
        pac *= i

    ans = []
    for j in range(len(str(pac))):
        ans.append(str(pac)[j])


    cnt=0
    for k in ans[::-1]:
        if k == "0":
            cnt+=1
        else:
            break

    print(cnt)
