import sys

x,y,w,h = map(int, sys.stdin.readline().split())

x_w = w-x
y_h = h-y
o_x = abs(0-x)
o_y = abs(0-y)

print(min(x_w, y_h, o_x, o_y))