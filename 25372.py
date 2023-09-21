N = int(input())
for i in range(N):
    num = input()
    if len(str(num)) < 6 or len(str(num)) > 9:
        print("no")
    else:
        print("yes")