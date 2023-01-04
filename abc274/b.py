# https://atcoder.jp/contests/abc274/tasks/abc274_b

H, W = map(int, input().split())
grids = [[] for _ in range(W)]
index = 0
for _ in range(H):
    C = input()
    for c in C:
        grids[index].append(c)
        if index == W - 1:
            index = 0
        else:
            index += 1
for grid in grids:
    print(grid.count("#"), end=" ")
