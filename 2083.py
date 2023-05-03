while(True):
    name, age, kg = map(str, input().split())
    if name == "#" and int(age) == 0 and int(kg) == 0 :
        break
    else :
        if int(age) > 17 or int(kg) >= 80:
            print(name ,"Senior")
        else :
            print(name ,"Junior")