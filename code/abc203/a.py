# https://atcoder.jp/contests/abc203/tasks/abc203_a

a, b, c = map(int, input().split())
if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(0)
