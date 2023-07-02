import sys

N = int(sys.stdin.readline())
ans = 1
board =[]

def search():
    global ans
    # 오른쪽 칸과 교환
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if board[i][j-1] == board[i][j]:
                cnt +=1
                ans = max(ans,cnt)
            else:
                cnt = 1

    # 아래 칸과 교환
    for j in range(N):
        cnt = 1
        for i in range(1,N):
            if board[i-1][j] == board[i][j]:
                cnt +=1
                ans = max(ans, cnt)
            else:
                cnt = 1


for i in range(0,N):
    board.append(list(str(sys.stdin.readline().rstrip())))
    

for j in range(len(board)):
    for k in range(len(board)):
        if k + 1 < N:
            board[j][k], board[j][k+1] = board[j][k+1], board[j][k]
            search()
            board[j][k], board[j][k+1] = board[j][k+1], board[j][k]
        
        if j + 1 < N:
            board[j][k], board[j+1][k] = board[j+1][k], board[j][k]
            search()
            board[j][k], board[j+1][k] = board[j+1][k], board[j][k]

print(board)
print(ans)