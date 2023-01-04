# https://atcoder.jp/contests/abc245/tasks/abc245_a

A, B, C, D = map(int, input().split())
if A > C:
    print("Aoki")
elif A < C:
    print("Takahashi")
elif B > D:
    print("Aoki")
elif B < D:
    print("Takahashi")
else:
    print("Takahashi")
