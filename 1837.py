import sys

P,K = map(int, sys.stdin.readline().split())
# --- 시간 초과 발생 ---
# ans = []
# for i in range(2,int(P ** 0.5)+1): # 2부터 P의 제급근까지의 숫자에서 소수 찾기
#     if P % i ==0 :
#         ans.append(i)


# if max(ans) <= K:
#     print("BAD", min(ans))
# else:
#     print("GOOD")

a = [False, False] + [True] * (K - 2)
for i in range(2, int(K ** 0.5) + 1):
    if a[i]:
        for j in range(i * 2, K, i):
            if a[j]:
                a[j] = False
flag = True
for i in range(2, K):
    if a[i]:
        if P % i == 0:
            flag = False
            break
 
if flag:
    print("GOOD")
else:
    print("BAD", i)