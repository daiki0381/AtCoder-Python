# https://atcoder.jp/contests/abc279/tasks/abc279_c


H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

transposed_s = list(zip(*S))
transposed_t = list(zip(*T))

if sorted(transposed_s) == sorted(transposed_t):
    print("Yes")
else:
    print("No")
