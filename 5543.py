s_b= int(input())
m_b= int(input())
l_b= int(input())
coke = int(input())
soda = int(input())
buger=[]
buger.append(s_b)
buger.append(m_b)
buger.append(l_b)
drink=[]
drink.append(coke)
drink.append(soda)
print(min(buger)+ min(drink) - 50)