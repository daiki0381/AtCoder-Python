# https://atcoder.jp/contests/abc024/tasks/abc024_a

A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
if S + T < K:
    print((A * S) + (T * B))
else:
    print((A * S) + (T * B) - ((S + T) * C))
