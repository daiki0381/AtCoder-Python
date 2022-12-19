# https://atcoder.jp/contests/abc137/tasks/abc137_a

A, B = map(int, input().split())
print(max(A + B, A - B, A * B))
