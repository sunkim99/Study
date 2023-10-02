import sys

train=[]
people= 0
for i in range(10):
    off, ride = map(int, sys.stdin.readline().split())
    people += ride
    people -= off
    train.append(people)

print(max(train))