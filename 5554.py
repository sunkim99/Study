import sys
second =0
min =0 
for i in range(0,4):
    second += int(sys.stdin.readline())

min, second = divmod(second,60)
print(min,second, sep='\n')