import sys

n = int(sys.stdin.readline())
num =0
for i in range(1,n+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        num += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        num += 1
    
print(num)