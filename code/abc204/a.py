# https://atcoder.jp/contests/abc204/tasks/abc204_a

x, y = map(int, input().split())
if x == y:
    print(x)
else:
    l = [0, 1, 2]
    l.remove(x)
    l.remove(y)
    print(l[0])
