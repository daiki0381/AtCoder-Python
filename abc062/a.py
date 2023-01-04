# https://atcoder.jp/contests/abc062/tasks/abc062_a

x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
if x in a:
    if y in a:
        print("Yes")
    else:
        print("No")
elif x in b:
    if y in b:
        print("Yes")
    else:
        print("No")
else:
    print("No")
