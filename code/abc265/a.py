# https://atcoder.jp/contests/abc265/tasks/abc265_a

X, Y, N = map(int, input().split())
if N < 3:
    print(N * X)
elif Y // 3 > X:
    print(N * X)
else:
    print((N // 3 * Y) + (N % 3 * X))
