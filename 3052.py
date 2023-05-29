import sys

answer=[]
for i in range(0,10):
    num = int(sys.stdin.readline())
    a,b = divmod(num, 42)
    answer.append(b)

print(len(set(answer)))
