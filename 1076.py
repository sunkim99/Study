register = {"black" : 1, 
            "brown" : 10, 
            "red" : 100, 
            "orange" : 1000, 
            "yellow" : 10000, 
            "green" : 100000, 
            "blue" : 1000000, 
            "violet" : 10000000, 
            "grey" : 100000000,  
            "white" : 1000000000}

register_val = ["black","brown","red", "orange","yellow", "green","blue", "violet", "grey" ,"white" ]
num = ''
for i in range(0,2):
    color = str(input())
    num += str(register_val.index(color))

color = str(input())
num = int(num) * register.get(color)  
print(num)
