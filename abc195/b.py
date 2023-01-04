# https://atcoder.jp/contests/abc195/tasks/abc195_b

A, B, _W = map(int, input().split())
W = 1000 * _W
quantity = []

for i in range(1, 10**6 + 1):
    if A * i <= W <= B * i:
        quantity.append(i)

if len(quantity) == 0:
    print("UNSATISFIABLE")
else:
    print(min(quantity))
    print(max(quantity))
