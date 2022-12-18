# https://atcoder.jp/contests/abc025/tasks/abc025_a

S = input()
N = int(input())
nickname_list = []
for i in range(5):
    for s in S:
        nickname_list.append(S[i] + s)
print(nickname_list[N - 1])
