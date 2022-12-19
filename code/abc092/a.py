# https://atcoder.jp/contests/abc092/tasks/abc092_a

A, B, C, D = [int(input()) for _ in range(4)]
print(min(A + C, B + C, A + D, B + D))
