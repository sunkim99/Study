a,b = map(int, input().split())

sum =0
minus=0
if a+b < 0 or a-b <0 or (a+b)%2 :
    print(-1)

else:
    sum = (a+b) //2
    minus = a-sum
    print(max(sum, minus), min(sum,minus))