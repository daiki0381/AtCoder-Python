# https://atcoder.jp/contests/abc282/tasks/abc282_c

N = int(input())
S = list(input())
is_bundled = False

for i in range(N):
    if S[i] == '"' and not is_bundled:
        is_bundled = True
    elif S[i] == '"' and is_bundled:
        is_bundled = False

    if S[i] == ',' and not is_bundled:
        S[i] = '.'

print("".join(S))
