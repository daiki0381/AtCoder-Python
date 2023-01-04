# https://atcoder.jp/contests/abc208/tasks/abc208_a

A, B = map(int, input().split())
if A <= B <= 6 * A:
    print("Yes")
else:
    print("No")
