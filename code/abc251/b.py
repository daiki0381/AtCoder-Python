# https://atcoder.jp/contests/abc251/tasks/abc251_b

from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))
ans = set()

for i in A:
    if i <= W:
        ans.add(i)

combs_2 = list(combinations(A, 2))
for j in combs_2:
    total = sum(j)
    if total <= W:
        ans.add(total)

combs_3 = list(combinations(A, 3))
for k in combs_3:
    total = sum(k)
    if total <= W:
        ans.add(total)

print(len(ans))
