dial = list(input())

Num= ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time =0

for i in dial:
    for j in Num:
        if i in j :
            time += Num.index(j) + 3

print(time)