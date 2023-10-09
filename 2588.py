num1 = int(input())
num2 = int(input())
num2 = str(num2)
mul_list =[]
for i in range(len(num2),0,-1):
    mul = num1 * int(num2[i-1])
    print(mul)

print(num1 * int(num2))
