import sys


N = int(sys.stdin.readline())

num = 0
for i in range(1,N+1):
    if i == 1:
        num += 5 
    else:
        num = num + (i+1) + (i*2)
    

print(int(num % 45678))