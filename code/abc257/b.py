# https://atcoder.jp/contests/abc257/tasks/abc257_b

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = map(int, input().split())

for l in L:
    if A[l - 1] < N and A.count(A[l - 1] + 1) == 0:
        A[l - 1] = A[l - 1] + 1
    else:
        continue

print(*A)
