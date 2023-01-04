# https://atcoder.jp/contests/abc187/tasks/abc187_a

A, B = input().split()
sum_a = sum(map(int, A))
sum_b = sum(map(int, B))
print(max(sum_a, sum_b))
