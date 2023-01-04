# https://atcoder.jp/contests/dp/tasks/dp_d

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N + 1)]

# 1番目
for i in range(W + 1):
    if i >= wv[0][0]:
        dp[1][i] = wv[0][1]

# 2番目以降
for i in range(2, N + 1):
    for j in range(W + 1):
        no_choice = dp[i - 1][j]
        if j < wv[i - 1][0]:
            dp[i][j] = no_choice
        else:
            # 1つ上の段のi番目のw分戻った列のv+i番目のv
            choice = dp[i - 1][j - wv[i - 1][0]] + wv[i - 1][1]
            dp[i][j] = max(no_choice, choice)

print(dp[N][W])
