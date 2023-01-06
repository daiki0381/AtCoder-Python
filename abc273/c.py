# https://atcoder.jp/contests/abc273/tasks/abc273_c

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))[::-1]
counter = Counter(A)

for b in B:
    print(counter[b])

for i in range(N - len(B)):
    print(0)
