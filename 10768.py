month = int(input())
day = int(input())

if month > 2:
    print("After")
else:
    if month == 2:
        if day < 18:
            print("Before")
        elif day == 18:
            print("Special")
        else:
            print("After")
    else:
        print("Before")
