# https://atcoder.jp/contests/abc280/tasks/abc280_a

H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for s in S:
    ans += s.count("#")
print(ans)
