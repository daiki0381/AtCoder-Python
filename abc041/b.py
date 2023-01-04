# https://atcoder.jp/contests/abc041/tasks/abc041_b

A, B, C = map(int, input().split())
X = A * B * C
print(X % (10 ** 9 + 7))
