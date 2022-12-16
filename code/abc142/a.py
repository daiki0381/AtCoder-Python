# https://atcoder.jp/contests/abc142/tasks/abc142_a

N = int(input())
if N == 1:
    print(1.0000000000)
elif N % 2 == 0:
    print(0.5000000000)
else:
    print(((N // 2) + 1) / N)
