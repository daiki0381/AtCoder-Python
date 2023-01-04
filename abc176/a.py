# https://atcoder.jp/contests/abc176/tasks/abc176_a

N, X, T = map(int, input().split())
if N % X == 0:
    print(N // X * T)
else:
    print((N // X + 1) * T)
