for i in range(3):
    yut = list(map(int, input().split()))
    mal = yut.count(0) # 배(0)
    mal_mo = yut.count(1) # 등(1)

    if mal == 1:
        print("A")
    elif mal == 2:
        print("B")
    elif mal == 3:
        print("C")
    elif mal == 4:
        print("D")
    elif mal == 0 and mal_mo == 4:
        print("E")