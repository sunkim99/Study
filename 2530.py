import sys
h,m,s = map(int,input().split())
time = int(sys.stdin.readline())
a__m, a__s= divmod(time, 60)
s += a__s
m += a__m

while True:
    if s > 59:
        a_s, ss = divmod(s, 60)
        m += a_s
        s = ss
    else:
        break

while True:
    if m > 59:
        a_m, mm = divmod(m, 60)
        h += a_m
        m = mm
    else:
        break
while True:
    if h >= 24:
        h1, hh = divmod(h, 24)
        h = hh
    else:
        break
print(h,m,s)
