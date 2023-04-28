word = input()
ans = ''
for i in word:
    if i.isupper() :
        ans += i.lower()
    else:
        ans+= i.upper()

print(ans)