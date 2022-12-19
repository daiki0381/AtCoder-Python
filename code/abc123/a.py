# https://atcoder.jp/contests/abc123/tasks/abc123_a

a, b, c, d, e, k = [int(input()) for _ in range(6)]
if e - a <= k:
    print("Yay!")
else:
    print(":(")
