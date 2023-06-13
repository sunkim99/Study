import sys
import collections

word = sys.stdin.readline().rstrip() # '\n'이 들어가는것을 막기위해 rstrip()추가
word = word.upper()

count = collections.Counter(word)
# print(max(count.keys()))  # 가장큰 알파벳 (a->z) 순서
# print(max(count.values()))
max =max(count.values()) 

ans = []
for key,val in count.items():
    if val == max:
        ans.append(key)
    else:
        pass

if len(ans) >=2 :
    print("?")
else:
    print(str(ans[0]))
