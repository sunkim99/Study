import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
m_list= list(map(int, sys.stdin.readline().split()))

ans = []

for i in m_list:
    l = bisect_left(n_list, i)
    r = bisect_right(n_list, i)
    ans.append(abs(r-l))

        
print(' '.join(map(str,ans)))