# https://atcoder.jp/contests/abc270/tasks/abc270_b

X, Y, Z = map(int, input().split())
if 0 < Y < X < Z or 0 > Y > X > Z or 0 < Y < Z < X or  X < Z < Y < 0:
    print(-1)
elif Z < 0 < Y < X or X < Y < 0 < Z:
    print(abs(X) + abs(Z) * 2)
else:
    print(abs(X))
