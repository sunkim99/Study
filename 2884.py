hour, min = map(int, input().split())

if min >= 45 :
    print(hour , min-45)
else:
    min = 60-45+min
    hour -= 1
    a,b = divmod(hour,24)
    print(b,min)