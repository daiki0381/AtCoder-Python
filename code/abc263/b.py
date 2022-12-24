# https://atcoder.jp/contests/abc263/tasks/abc263_b

N = int(input())
P = list(map(int, input().split()))
current_ancestor_index = P[-1]
ans = 1

while True:
    if P[-1] == 1:
        break
    if P[current_ancestor_index - 2] == 1:
        ans += 1
        break
    else:
        ans += 1
        current_ancestor_index = P[current_ancestor_index - 2]
print(ans)
