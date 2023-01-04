# https://atcoder.jp/contests/abc202/tasks/abc202_b

S = input()
print(S.replace("6", "x").replace("9", "6").replace("x", "9")[::-1])
