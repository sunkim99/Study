import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

lo = 0
high = max(tree)
mid = (lo + high) //2

def get_total_tree(h):
    ret = 0
    for i in tree:
        if i > h:
            ret += i-h
    return ret

ans = 0 
while lo <= high:
    if get_total_tree(mid) >= M:
        ans = mid
        lo = mid +1
    else:
        high = mid -1

    mid = (lo + high) //2

print(ans)