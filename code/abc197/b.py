# https://atcoder.jp/contests/abc197/tasks/abc197_b

H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [input() for _ in range(H)]
ans = 1

# 上
for col in reversed(range(X)):
    if S[col][Y] == "#":
        break
    else:
        ans += 1

# 下
for col in range(X + 1, H):
    if S[col][Y] == "#":
        break
    else:
        ans += 1

# 左
for row in reversed(range(Y)):
    if S[X][row] == "#":
        break
    else:
        ans += 1

# 右
for row in range(Y + 1, W):
    if S[X][row] == "#":
        break
    else:
        ans += 1

print(ans)
