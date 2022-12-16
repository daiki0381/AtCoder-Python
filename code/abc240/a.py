# https://atcoder.jp/contests/abc240/tasks/abc240_a

a, b = map(int, input().split())
if a == 1 and (b == 10 or b == 2):
    print("Yes")
elif a == 10 and (b == 9 or b == 1):
    print("Yes")
elif b == 1 and (a == 10 or a == 2):
    print("Yes")
elif b == 10 and (a == 9 or a == 1):
    print("Yes")
elif a == b - 1 or a == b + 1:
    print("Yes")
else:
    print("No")
