import sys

L = int(sys.stdin.readline())
ans =[]
for i in range(0,L):
    left =[]
    right =[]
    for j in str(sys.stdin.readline().rstrip()):
        if j == "<":
            if left:
                # left라는 배열이 비어있지 않다면,
                right.append(left.pop())
        elif j == ">":
            if right:
                # right가 비어있지 않다면,
                left.append(right.pop())
        elif j == "-":
            if left:
                left.pop()
        else: # 그냥 문자열일때,
            left.append(j)
        
    ans.append(''.join(left)+''.join(reversed(right)))
    # right에 대해서 reversed를 하는 이유는
    # 스택은 filo = 먼저들어간게 나중에 나오기때문에 
    # right 는 역순으로 출력한다.

for k in ans:
    print(k)