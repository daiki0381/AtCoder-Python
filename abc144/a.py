# https://atcoder.jp/contests/abc144/tasks/abc144_a

A, B = map(int, input().split())
if 1 <= A <= 9 and 1 <= B <= 9:
    print(A * B)
else:
    print(-1)
