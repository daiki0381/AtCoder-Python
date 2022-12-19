# https://atcoder.jp/contests/abc042/tasks/abc042_a

ABC = list(map(int, input().split()))
if ABC.count(5) == 2 and ABC.count(7) == 1:
    print("YES")
else:
    print("NO")
