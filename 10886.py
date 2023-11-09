N = int(input())
num_list =[]
for i in range(N):
    num = int(input())
    num_list.append(num)

num_1 = num_list.count(1)
num_0 = num_list.count(0)

if num_0 > num_1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")