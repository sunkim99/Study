import sys
S = str(sys.stdin.readline())
answer=[]

for j in range(97,123):
    if chr(j) in S :
        answer.append(S.index(chr(j)))
    else:
        answer.append(-1)

for i in answer:
    print(i, end=' ')


'''
아스키코드로 97번 = a
122번 = z 
아스키 코드 변환 함수 
ord() : 문자열을 아스키코드로 반환한다 
    괄호안에 문자를 넣으면, 그에 해당하는 아스키코드를 숫자로 반환한다.

chr() : 아스키코드를 문자열로 변환
    괄호안에 숫자를 넣으면 그 숫자의 아스키코드에 대응하는 문자를 반환한다.

print( end=' ') -> 문자열 끝에 개행문자 대신 공백 추가한뒤, 같은 줄에서 출력
'''