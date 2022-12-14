# https://atcoder.jp/contests/abc096/tasks/abc096_a

a, b = map(int, input().split())
if a <= b:
    print(a)
else:
    print(a - 1)
