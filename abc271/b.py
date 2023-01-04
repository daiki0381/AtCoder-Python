# https://atcoder.jp/contests/abc271/tasks/abc271_b

N, Q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
S = [list(map(int, input().split())) for _ in range(Q)]
for s in S:
    print(L[s[0] - 1][s[1]])
