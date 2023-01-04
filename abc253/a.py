# https://atcoder.jp/contests/abc253/tasks/abc253_a

a, b, c = map(int, input().split())
if a == b == c:
    print("Yes")
elif a <= b <= c or c <= b <= a:
    print("Yes")
else:
    print("No")
