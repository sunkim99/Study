import sys

N, B = map(str, sys.stdin.readline().split())

print(int(N, int(B)))

'''
B진법수 N을 10진법으로 출력

int(변환할string, n진법(int형으로 입력해야함))
-> ZZZZZ가 36진법으로 되어있는데 이걸 10진법으로 변환해 출력
'''