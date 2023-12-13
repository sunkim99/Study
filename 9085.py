T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(sum(num_list))