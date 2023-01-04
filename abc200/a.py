# https://atcoder.jp/contests/abc200/tasks/abc200_a

N = int(input())
if N % 100 == 0:
    print(N // 100)
else:
    print(N // 100 + 1)
