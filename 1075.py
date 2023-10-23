
N = int(input())
F = int(input())

tmp = str(N)[:-2] +'00'
tmp = int(tmp)

while True:
    if tmp % F ==0:
        break
    tmp +=1

print(str(tmp)[-2:])