# https://atcoder.jp/contests/abc252/tasks/abc252_b

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_num = max(A)
max_index_list = []

for a_index, a in enumerate(A):
    if a == max_num:
        max_index_list.append(a_index + 1)

for b in B:
    if max_index_list.count(b) != 0:
        print("Yes")
        break
else:
    print("No")
