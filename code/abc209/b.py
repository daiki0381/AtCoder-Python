# https://atcoder.jp/contests/abc209/tasks/abc209_b

N, X = map(int, input().split())
A = list(map(int, input().split()))

for a_index, a in enumerate(A):
    if (a_index + 1) % 2 == 0:
        X = X - a + 1
    else:
        X -= a

if X < 0:
    print("No")
else:
    print("Yes")
