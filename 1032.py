N = int(input())
word = list(input())

for _ in range(N-1):
    word2 = str(input())
    for j in range(len(word)):
        if word[j] == word2[j]:
            continue
        else:
            word[j] = "?"

print(''.join(word))