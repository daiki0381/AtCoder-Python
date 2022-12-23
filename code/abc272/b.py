# https://atcoder.jp/contests/abc272/tasks/abc272_b

N, M = map(int, input().split())
pairs = set()

for _ in range(M):
    k_x_list = list(map(int, input().split()))
    x_list = k_x_list[1:]
    for i in range(len(x_list)):
        for x in x_list:
            if x_list[i] == x:
                continue
            else:
                pairs.add(tuple(sorted([x_list[i], x])))

if N * (N - 1) // 2 == len(pairs):
    print("Yes")
else:
    print("No")
