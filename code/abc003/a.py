# https://atcoder.jp/contests/abc003/tasks/abc003_1

N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i * 10000 / N
print(ans)
