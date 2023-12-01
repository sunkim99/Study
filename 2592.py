number =[]
for i in range(10):
    num=int(input())
    number.append(num)

print(int(sum(number) / len(number)))
print(max(number, key=number.count))