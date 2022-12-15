# https://atcoder.jp/contests/abc242/tasks/abc242_a

A, B, C, X = map(int, input().split())
if X <= A:
    print(1.000000000000)
elif X > B:
    print(0.000000000000)
else:
    print(C / (B - A))
