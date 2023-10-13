import sys


def round2(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(sys.stdin.readline())

if n :
    level = []
    for i in range(n):
        num = int(sys.stdin.readline())
        level.append(num)

    pec = round2(n * 0.15)
    level.sort()
    print(round2( sum(level[pec:-pec] if pec else level) / (n-2 * pec) ))

else:
    print(0) 