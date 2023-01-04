# https://atcoder.jp/contests/abc022/tasks/abc022_a

N, S, T = map(int, input().split())
W = int(input())
l = [int(input()) for _ in range(N - 1)]
if S <= W <= T:
    ans = 1
else:
    ans = 0
for i in l:
    W += i
    if S <= W <= T:
        ans += 1
print(ans)
