# https://atcoder.jp/contests/abc224/tasks/abc224_b

from itertools import combinations

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

i_combs = list(combinations([i for i in range(1, H + 1)], 2))
j_combs = list(combinations([i for i in range(1, W + 1)], 2))
i_j_combs = []

for i_comb in i_combs:
    if i_comb[0] > i_comb[1]:
        i_combs.remove(i_comb)

for j_comb in j_combs:
    if j_comb[0] > j_comb[1]:
        j_combs.remove(j_comb)

for i_comb in i_combs:
    for j_comb in j_combs:
        i_j_combs.append(i_comb + j_comb)

for i_j_comb in i_j_combs:
    if (
        A[i_j_comb[0] - 1][i_j_comb[2] - 1] + A[i_j_comb[1] - 1][i_j_comb[3] - 1]
        > A[i_j_comb[1] - 1][i_j_comb[2] - 1] + A[i_j_comb[0] - 1][i_j_comb[3] - 1]
    ):
        print("No")
        break
else:
    print("Yes")
