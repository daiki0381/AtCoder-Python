# https://atcoder.jp/contests/abc275/tasks/abc275_c

from itertools import combinations

squares = set()

# ①ポーンが置いてある座標を全列挙
for i in range(9):
    S = input()
    for j in range(9):
        if S[j] == "#":
            squares.add((i, j))

# ②ポーンが置いてある座標の4頂点の組み合わせを全列挙
patterns = combinations(squares, 4)
ans = 0

# 正方形を判定するメソッド
def judge_square(square):
    distances = []
    for i, j in combinations(square, 2):
        distances.append((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
    distances.sort()
    return (
        distances[0] == distances[1] == distances[2] == distances[3]
        and (distances[4] == distances[0] * 2)
        and (distances[5] == distances[0] * 2)
    )


# ③正方形の個数を数える
for pattern in patterns:
    if judge_square(pattern):
        ans += 1

print(ans)
