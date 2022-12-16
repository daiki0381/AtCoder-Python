# https://atcoder.jp/contests/abc223/tasks/abc223_a

X = int(input())
if X < 100:
    print("No")
elif X % 100 == 0:
    print("Yes")
else:
    print("No")
