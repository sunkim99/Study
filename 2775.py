T = int(input())
for _ in range(0,T):
    K = int(input())
    n = int(input())
    f = [x for x in range(1,n+1)]
    for k in range(K):
        for i in range(1,n):
            f[i] += f[i-1]

    print(f[-1])
