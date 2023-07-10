import sys


student = []
for i in range(1,31):
    student.append(i)


for i in range(1,29):
    n= int(input())
    if n in student:
        student.remove(n)

    
for j in student:
    print(j)
