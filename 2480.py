dice1, dice2, dice3 = map(int, input().split())

if dice1 == dice2 == dice3 :
    print(10000 + (dice1)*1000)
elif (dice1 == dice2 and dice1!= dice3) or (dice2 != dice1 and dice2 ==dice3) or (dice3 == dice1 and dice3 != dice2):
    if (dice1 == dice2) and (dice1 != dice3):
        print(1000 +(dice1)*100)
    elif (dice2 != dice3) and (dice2== dice1):
        print(1000 +(dice2)*100)
    else:
        print(1000 + (dice3)*100)

else:
    print(max(dice1,dice2,dice3) *100)