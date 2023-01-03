# https://atcoder.jp/contests/abc189/tasks/abc189_b

# ※浮動小数点数の演算は一般に誤差を含むので、整数同士の演算に変換する必要がある

from itertools import accumulate

N, X = map(int, input().split())
alcohol_intakes = []

for _ in range(N):
    V, P = map(int, input().split())
    alcohol_intakes.append(V * P)

cumulative_alcohol_intakes = [i for i in accumulate(alcohol_intakes)]

for cumulative_alcohol_intake_index, cumulative_alcohol_intake in enumerate(cumulative_alcohol_intakes):
    if 100 * X < cumulative_alcohol_intake:
        print(cumulative_alcohol_intake_index + 1)
        break
else:
    print(-1)
