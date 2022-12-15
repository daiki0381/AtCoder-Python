# https://atcoder.jp/contests/abc083/tasks/abc083_a

A, B, C, D = map(int, input().split())
if A + B > C + D:
    print("Left")
elif A + B < C + D:
    print("Right")
else:
    print("Balanced")
