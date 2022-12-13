# https://atcoder.jp/contests/abc075/tasks/abc075_a

A, B, C = map(int, input().split())

if A == B:
    print(C)
elif A == C:
    print(B)
elif B == C:
    print(A)
