# https://atcoder.jp/contests/abc277/tasks/abc277_b

N = int(input())
S = [input() for _ in range(N)]
wrong_num = 0
for s in S:
    if s[0] not in "HDCS":
        wrong_num += 1
    if s[1] not in "A23456789TJQK":
        wrong_num += 1
    if S.count(s) != 1:
        wrong_num += 1
if wrong_num == 0:
    print("Yes")
else:
    print("No")
