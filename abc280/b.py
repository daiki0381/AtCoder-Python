# https://atcoder.jp/contests/abc280/tasks/abc280_b

N = int(input())
S = map(int, input().split())
ans = []
for s in S:
    if len(ans) == 0:
        ans.append(s)
    else:
        ans.append(s - sum(ans))
print(*ans)
