n = int(input())
    
for i in range(1, n*2+1):
    if i % 2 == 0:
        print(' *' * int(n/2))
    else:
        if n % 2 == 1:
            print('* ' * int(n/2) + '*')
        else:
            print('* ' * int(n/2))