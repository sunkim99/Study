N, W, H = map(int, input().split())
d = (W**2 + H**2)**0.5
for _ in range(N):
    n = int(input())
    if n <= d :
        print("DA")
    else : 
        print("NE")