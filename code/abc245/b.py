# https://atcoder.jp/contests/abc245/tasks/abc245_b

N = int(input())
A = list(map(int, input().split()))

for n in range(2001):
    if A.count(n) == 0:
        print(n)
        break
