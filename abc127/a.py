# https://atcoder.jp/contests/abc127/tasks/abc127_a

A, B = map(int, input().split())
if A >= 13:
    print(B)
elif A >= 6 and A <= 12:
    print(B // 2)
else:
    print(0)
