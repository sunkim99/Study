import sys

N = int(sys.stdin.readline())

list =[]
for i in range(0,N):
    age, name = map(str, sys.stdin.readline().split())
    list.append([int(age), i, name])

list = sorted(list)

for j in range(len(list)):
    print(list[j][0], list[j][2])


