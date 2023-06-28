import sys

N = int(sys.stdin.readline())
b = dict()

for i in range(0,N):
    book = str(sys.stdin.readline())
    if book in b:
        b[book] += 1
    else:
        b[book] = 1

max = max(b.values())
ans = []
for key, value in b.items():
    if max == value:
        ans.append(key)

ans = sorted(ans) # 여러개일경우 사전순으로 가장 앞에있는 제목 == 정렬하기
print(ans[0])