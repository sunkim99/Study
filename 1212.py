import sys

num = str(sys.stdin.readline())


print(bin(int(num,8))[2:])

'''
314 -> 0b11001100
맨앞 2자리에 이집법을 의미히난 0b가 붙는데, 이를 제외하고 출력
'''