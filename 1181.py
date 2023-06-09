import sys

N = int(sys.stdin.readline())

word =[]
for i in range(N):
    word.append(str(sys.stdin.readline()))

word= sorted(set(word))
word.sort(key=len)

for j in word:
    print(j, end='')