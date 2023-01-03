# https://atcoder.jp/contests/abc193/tasks/abc193_b

N = int(input())
times = []

for _ in range(N):
    A, P, X = map(int, input().split())
    if A + 0.5 < X:
        times.append(P)

if len(times) == 0:
    print(-1)
else:
    print(min(times))
