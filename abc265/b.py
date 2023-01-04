# https://atcoder.jp/contests/abc265/tasks/abc265_b

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

for xy in XY:
    A[xy[0] - 1] = A[xy[0] - 1] - xy[1]

for a in A:
    T -= a
    if T <= 0:
        break

if T <= 0:
    print("No")
else:
    print("Yes")
