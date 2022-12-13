# https://atcoder.jp/contests/abc148/tasks/abc148_a

A, B = [int(input()) for _ in range(2)]
l = [1, 2, 3]
l.remove(A)
l.remove(B)
print(*l)
