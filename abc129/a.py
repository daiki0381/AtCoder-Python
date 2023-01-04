# https://atcoder.jp/contests/abc129/tasks/abc129_a

P, Q, R = map(int, input().split())
print(min(P + Q, P + R, Q + R))
