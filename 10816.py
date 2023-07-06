# -----------------------------------------------------------------
# 이분탐색
# from bisect import bisect_left, bisect_right
# a = [2,3,6,6,6,10,12,15]
# l = bisect_left(a,6)
# print(l)
# r = bisect_right(a,6)
# print(r)
# # right - left 하면 배열에 목표 값이 몇 개가 있는지 알 수 있음.
# -----------------------------------------------------------------
import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
n_list = sorted(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

ans = []
for i in m_list:
    l = bisect_left(n_list, i)
    r = bisect_right(n_list, i)
    ans.append(r-l)

print(' '.join(map(str,ans)))