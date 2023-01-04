# https://atcoder.jp/contests/abc280/tasks/abc280_c

S = input() + "0"
T = input()
t_len = len(T)

for i in range(t_len):
    if S[i] != T[i]:
        print(i + 1)
        break
