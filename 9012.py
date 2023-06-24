import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    ans =[] 
    vps = list(str(sys.stdin.readline()).rstrip()) # rstrip() 은 리스트 마지막에 '\n' 을 제거하기 위함
    for j in range(len(vps)):
        if not ans: # 빈리스트라면 바로 넣어주기
            ans.append(vps[j])
        else:
            ans.append(vps[j])
            if (ans[-2] =="(") and (ans[-1] ==")"):
                ans.pop()
                ans.pop()

    if not ans: #비었다면 vps
        print("YES")
    else:
        print("NO")
