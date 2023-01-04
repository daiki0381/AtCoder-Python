# https://atcoder.jp/contests/abc234/tasks/abc234_b

import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

length_list = []

for i in range(N):
    for j in range(i + 1, N):
        length_list.append(
            math.sqrt((XY[j][0] - XY[i][0]) ** 2 + (XY[j][1] - XY[i][1]) ** 2)
        )

print(max(length_list))
