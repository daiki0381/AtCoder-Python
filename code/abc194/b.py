# https://atcoder.jp/contests/abc194/tasks/abc194_b

N = int(input())
A = []
B = []
times = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(N):
    for j in range(N):
        if i == j:
            times.append(A[i] + B[j])
        else:
            times.append(max(A[i], B[j]))

print(min(times))
