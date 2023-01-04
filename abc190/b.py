# https://atcoder.jp/contests/abc190/tasks/abc190_b

N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

for xy in XY:
    if xy[0] < S and xy[1] > D:
        print("Yes")
        break
else:
    print("No")
