# https://atcoder.jp/contests/abc120/tasks/abc120_a

A, B, C = map(int, input().split())
if B // A >= C:
    print(C)
else:
    print(B // A)
