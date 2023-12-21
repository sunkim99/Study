import sys

T = int(sys.stdin.readline())

for _ in range(T):
    word = list(map(str, sys.stdin.readline().split()))
    sentence =[]

    for words in word:
        sentence.append(words[::-1])

    print(" ".join(sentence))