# https://atcoder.jp/contests/abc259/tasks/abc259_a

N, M, X, T, D = map(int, input().split())
if M >= X and M <= N:
    print(T)
else:
    print((T - ((X - 1) * D)) + ((M - 1) * D))
