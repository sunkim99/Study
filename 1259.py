import sys


ans =[]
while(True):
    N = int(sys.stdin.readline())
    if N !=0:
        p = str(N)[::-1]
        if int(p) == N:
            ans.append("yes")
        else:
            ans.append("no")

    elif N == 0:
        for i in ans:
            print(i)
        break
    