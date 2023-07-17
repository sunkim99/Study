import sys


N = int(sys.stdin.readline())
ans = []
for i in range(0,N):
    name, kor, eng, math =map(str, sys.stdin.readline().split())
    ans.append([name, int(kor), int(eng), int(math)])
    
ans = sorted(ans, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in ans:
    print(i[0])