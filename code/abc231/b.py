# https://atcoder.jp/contests/abc231/tasks/abc231_b

N = int(input())
S = [input() for _ in range(N)]

max_num = 0
candidate = ""

for s in S:
    if S.count(s) > max_num:
        max_num = S.count(s)
        candidate = s

print(candidate)
