# https://atcoder.jp/contests/abc210/tasks/abc210_b

N = int(input())
S = input()

if (S.find("1") + 1) % 2 == 0:
    print("Aoki")
else:
    print("Takahashi")
