L= int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

e = A//C
f = B//D
if e>f :
    if A%C ==0:
        print(L-e)
    else:
        print(L-1-e)

else:
    if B%D ==0:
        print(L-f)
    else:
        print(L-1-f)