# https://atcoder.jp/contests/abc047/tasks/abc047_a

a, b, c = sorted(map(int, input().split()))
if a + b == c:
    print("Yes")
else:
    print("No")
