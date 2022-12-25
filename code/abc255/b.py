# https://atcoder.jp/contests/abc255/tasks/abc255_b

import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

distances = []

for n in range(N):
    temp = []
    for k in range(K):
        temp.append(
            math.sqrt(
                (XY[A[k] - 1][0] - XY[n][0]) ** 2 + (XY[A[k] - 1][1] - XY[n][1]) ** 2
            )
        )
    if len(temp) != 0:
        distances.append(min(temp))
print(max(distances))
