# https://atcoder.jp/contests/abc216/tasks/abc216_a

X, Y = input().split(".")
if 0 <= int(Y) <= 2:
    print(X + "-")
elif 3 <= int(Y) <= 6:
    print(X)
else:
    print(X + "+")
