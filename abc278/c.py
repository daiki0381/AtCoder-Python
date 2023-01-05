# https://atcoder.jp/contests/abc278/tasks/abc278_c

# N ≤ 10 ** 9の場合、配列だとTLEするので、データ構造をsetにする必要がある

N, Q = map(int, input().split())
follows = set()

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        follows.add((a, b))
    elif t == 2:
        if (a, b) in follows:
            follows.remove((a, b))
    else:
        if (a, b) in follows and (b, a) in follows:
            print("Yes")
        else:
            print("No")
