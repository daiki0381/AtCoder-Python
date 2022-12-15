# https://atcoder.jp/contests/abc190/tasks/abc190_a

A, B, C = map(int, input().split())
if A > B:
    print("Takahashi")
elif A < B:
    print("Aoki")
elif A == B and C == 0:
    print("Aoki")
else:
    print("Takahashi")
