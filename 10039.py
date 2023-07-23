
score = []
for i in range(0,5):
    num = int(input())
    if num < 40:
        num = 40

    score.append(num)

print(int(sum(score)/5 ))