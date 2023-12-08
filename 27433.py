N = int(input())

num =1
if N == 0:
    print(num)
else:

    for i in range(1, N+1):
        num *= i
    print(num)