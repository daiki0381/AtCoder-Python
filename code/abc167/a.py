# https://atcoder.jp/contests/abc167/tasks/abc167_a

S, T = [input() for _ in range(2)]
if S == T[:-1]:
    print("Yes")
else:
    print("No")
