N = int(input())
cnt = 0
for i in range(N):
    word = str(input())
    word_list = []
    if len(word) ==1:
        cnt +=1 
    else:
        for j in range(len(word)):
            if j ==0:
                word_list.append(word[j])
            elif j > 0:
                if word[j] == word[j-1]:
                    word_list.append(word[j])
                    if j == len(word) -1:
                        cnt +=1
                elif word[j] != word[j-1]:
                    if word[j] not in word_list:
                        if j == len(word)-1:
                            cnt +=1
                        else:
                            word_list.append(word[j])
                    elif word[j] in word_list:
                        break
print(cnt)