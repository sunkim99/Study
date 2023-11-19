import sys

D, H, W = map(int,sys.stdin.readline().split())

'''
d = tv 대각선 길이
h = tv 높이
w = tv 너비비율
'''

r = D / (H**2 + W**2) ** 0.5
print(int(H*r), int(W*r))