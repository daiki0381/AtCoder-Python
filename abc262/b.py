# https://atcoder.jp/contests/abc262/tasks/abc262_b

N, M = map(int, input().split())
table = [[False] * N for _ in range(N)]

"""
Nが3の場合
[
    [False, False, False],
    [False, False, False],
    [False, False, False],
]
"""

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    table[U][V] = True
    table[V][U] = True

ans = 0

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if table[a][b] == True and table[a][c] == True and table[b][c] == True:
                ans += 1
print(ans)
