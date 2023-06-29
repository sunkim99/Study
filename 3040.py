# 조합 (combination)
# n개의 수 중에서 r개를 뽑는 가지 수 = nCr
# from itertools import combinations

# arr = [0,1,2,3]
# for i in combinations(arr,2):
#     print(i)
# ----------------------------------------
from itertools import combinations
import sys

num =[]
for i in range(0,9):
    num.append(int(sys.stdin.readline()))

for j in combinations(num, 7):
    if sum(j) == 100:
        for k in j:
            print(k)
        break