# 1. 시간초과
# import sys

# n = int(sys.stdin.readline())

# log = []
# for i in range(0,n):
#     name, stay = map(str, sys.stdin.readline().split())
#     if not(name in log):
#         # log에 들어가있지 않으면 
#         if stay == "enter":
#             log.append(name)
#         else:
#             pass
#     else:
#         # log에 들어가있고, 상태가 stay 라면
#         if stay == "leave":
#             log.remove(name)

# log = sorted(log, reverse=True) # 현재 회사에 있는 사람의 이름을 사전순의 역순으로 정렬

# for j in range(len(log)):
#     print(log[j])
# ----------------------------------------------------------------
# 2. 시간초과
# import sys

# n = int(sys.stdin.readline())

# log = []
# for i in range(0,n):
#     name, stay = map(str, sys.stdin.readline().split())
#     if stay == "enter":
#         log.append(name)
#     else: # leave
#         if name in log:
#             log.remove(name)
#         else:
#             pass


# log = sorted(log, reverse=True) 
# # 현재 회사에 있는 사람의 이름을 사전순의 역순으로 정렬

# for j in range(len(log)):
#     print(log[j])
# ----------------------------------------------------------------


import sys

n = int(sys.stdin.readline())
log = set()
for i in range(0,n):
    name, stay = map(str, sys.stdin.readline().split())
    if stay == "enter":
        log.add(name)
    else:
        if name in log :
            # log에 name이 있다는 가정
            log.remove(name)

log = sorted(log, reverse=True)
for j in log:
    print(j)