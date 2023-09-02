s = int(input())


if s % 5 == 0:
    print(s//5)
else :
    p = 0
    while s > 0:
        s -=3
        p += 1
        if s % 5 ==0:
            p += s // 5
            print(p)
            break  
        elif s == 1 or s == 2:
            print(-1)
            break
        elif s == 0 :
            print(p)
            break