fbi =[]
for i in range(1,6):
    person = str(input())
    if "FBI" in person:
        fbi.append(i)
    
if fbi:
    print(*fbi)
else:
    print("HE GOT AWAY!")