# https://atcoder.jp/contests/abc214/tasks/abc214_a

N = int(input())
if N < 126:
    print(4)
elif N < 212:
    print(6)
else:
    print(8)
