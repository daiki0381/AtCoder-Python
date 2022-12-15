# https://atcoder.jp/contests/abc136/tasks/abc136_a

A, B, C = map(int, input().split())
if A - B < C:
    print(C - (A - B))
else:
    print(0)
