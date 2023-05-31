N = int(input())

score = list(map(int, input().split()))

ans = []
for i in score:
    ans.append(round(i / max(score)*100,2))


print(sum(ans)/N)