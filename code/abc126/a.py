# https://atcoder.jp/contests/abc126/tasks/abc126_a

N, K = map(int, input().split())
S = input()
l = []
for i in range(N):
    if i + 1 == K:
        l.append(S[i].lower())
    else:
        l.append(S[i])
print("".join(l))
