# https://atcoder.jp/contests/abc248/tasks/abc248_b

A, B, K = map(int, input().split())
ans = 0

while A < B:
    A = A * K
    ans += 1
print(ans)
