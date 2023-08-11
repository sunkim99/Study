T = input()
m = list(map(int, input().split()))

Y =0
M =0

for i in m:
    Y += (i //30 +1) * 10
    M += (i //60 +1) * 15

if M == Y :
    print("Y M {0}".format(Y))
elif M < Y :
    print("M {0}".format(M))
else:
    print("Y {0}".format(Y))