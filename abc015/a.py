# https://atcoder.jp/contests/abc015/tasks/abc015_1

A, B = [input() for _ in range(2)]
if len(A) < len(B):
    print(B)
else:
    print(A)
