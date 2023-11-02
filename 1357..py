X,Y = map(str,input().split())
X = X[::-1]
Y = Y[::-1]
n = int(X)+ int(Y)
n = int(str(n)[::-1])
print(n)