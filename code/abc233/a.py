# https://atcoder.jp/contests/abc233/tasks/abc233_a

import math

X, Y = map(int, input().split())
if X < Y:
    print(math.ceil((Y - X) / 10))
else:
    print(0)
