# https://atcoder.jp/contests/abc191/tasks/abc191_a

V, T, S, D = map(int, input().split())
if T < S < D / V or D / V < T < S:
    print("Yes")
else:
    print("No")
