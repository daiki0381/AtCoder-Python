# https://atcoder.jp/contests/abc254/tasks/abc254_b

N = int(input())

output_list = [[] for _ in range(N)]
col_num = 0

for i in range(N):
    col_num += 1
    for j in range(col_num):
        if j == 0 or j == i:
            output_list[i].append(1)
        else:
            output_list[i].append(output_list[i - 1][j - 1] + output_list[i - 1][j])

for output in output_list:
    print(*output)
