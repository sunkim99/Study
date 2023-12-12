ans = {}

for i in range(1,6):
    score = list(map(int, input().split()))
    ans[i] = sum(score)

print(max(ans, key=ans.get), max(ans.values()))