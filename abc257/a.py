# https://atcoder.jp/contests/abc257/tasks/abc257_a

N, X = map(int, input().split())
alphabet_list = []
for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for i in range(N):
        alphabet_list.append(alphabet)
print(alphabet_list[X - 1])
