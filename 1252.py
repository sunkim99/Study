a,b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)
num = a+b
print(bin(num)[2:])
