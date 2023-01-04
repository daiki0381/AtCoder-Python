# https://atcoder.jp/contests/abc237/tasks/abc237_b

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[] for _ in range(W)]

for col in range(H):
    for row in range(W):
        B[row].append(A[col][row])

for b in B:
    print(*b)
