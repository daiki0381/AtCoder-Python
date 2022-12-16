# https://atcoder.jp/contests/abc014/tasks/abc014_1

a, b = [int(input()) for _ in range(2)]
if a % b == 0:
    print(0)
elif a < b:
    print(b - a)
else:
    print(b - (a % b))
