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

for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if (
                table[a - 1][b - 1] == True
                and table[a - 1][c - 1] == True
                and table[b - 1][c - 1] == True
            ):
                ans += 1
print(ans)
