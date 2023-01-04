# https://atcoder.jp/contests/abc115/tasks/abc115_a

D = int(input())
if D == 25:
    print("Christmas")
elif D == 24:
    print("Christmas" + " Eve" * 1)
elif D == 23:
    print("Christmas" + " Eve" * 2)
else:
    print("Christmas" + " Eve" * 3)
