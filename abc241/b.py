# https://atcoder.jp/contests/abc241/tasks/abc241_b

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    if B.count(b) > A.count(b):
        print("No")
        break
else:
    print("Yes")
