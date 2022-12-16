# https://atcoder.jp/contests/abc173/tasks/abc173_a

N = int(input())
if N % 1000 == 0:
    print(0)
else:
    print(1000 - (N % 1000))
