import sys
N = int(sys.stdin.readline())
com =0 
for i in range(N):
    plug = int(sys.stdin.readline())
    com += plug
print(com- (N-1))