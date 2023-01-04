# https://atcoder.jp/contests/abc226/tasks/abc226_b

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

ans_list = []

for l in L:
    ans_list.append(tuple(l[1:]))

print(len(set(ans_list)))
