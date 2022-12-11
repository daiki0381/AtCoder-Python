# 問題 https://atcoder.jp/contests/abc055/tasks/abc055_b

import math

N = int(input())
print(math.factorial(N) % (10 ** 9 + 7))
