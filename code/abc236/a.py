# https://atcoder.jp/contests/abc236/tasks/abc236_a

S = list(input())
a, b = map(int, input().split())
s_a = S[a - 1]
s_b = S[b - 1]
S[a - 1] = s_b
S[b - 1] = s_a
print("".join(S))
