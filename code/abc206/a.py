# https://atcoder.jp/contests/abc206/tasks/abc206_a

N = int(input())
if int(1.08 * N) > 206:
    print(":(")
elif int(1.08 * N) < 206:
    print("Yay!")
else:
    print("so-so")
