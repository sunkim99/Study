import sys

N = int(sys.stdin.readline())

loc = []
for i in range(0,N):
    x,y = map(int,sys.stdin.readline().split())
    loc.append([x,y])

loc = sorted(loc)
for j in range(len(loc)):
    print(loc[j][0], loc[j][1])