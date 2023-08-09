a,b,c =map(int, input().split())

ans =[]
ans.append(a)
ans.append(b)
ans.append(c)


print(' '.join(map(str, sorted(ans))))