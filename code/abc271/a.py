# https://atcoder.jp/contests/abc271/tasks/abc271_a

N = int(input())
if N <= 15:
    print("0" + f"{N:X}")
else:
    print(f"{N:X}")
