# https://atcoder.jp/contests/abc273/tasks/abc273_b

from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())
for k in range(1, K + 1):
    X = int(Decimal(X).quantize(Decimal('1E' + str(k)), rounding=ROUND_HALF_UP))
print(X)
