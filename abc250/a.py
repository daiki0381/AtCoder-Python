# https://atcoder.jp/contests/abc250/tasks/abc250_a

H, W = map(int, input().split())
R, C = map(int, input().split())
square_num = 0
if R - 1 > 0:
    square_num += 1
if C + 1 <= W:
    square_num += 1
if R + 1 <= H:
    square_num += 1
if C - 1 > 0:
    square_num += 1
print(square_num)
