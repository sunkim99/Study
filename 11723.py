import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)


# discard(), remove() 는 엘리먼트를 삭제하는 동작 수행
# 차이점은
# remove()는 엘리먼트가 존재하지 않으면 KeyError가 발생하고
# discard()메소드는 엘리먼트가 없어도 정상종료를 한다.

# remove()는 실제 존재하는 대상을 지우는 동작에, 
# discard()는 존재하지 않음을 보장하려고 할때 사용하면 될 것 같다.

