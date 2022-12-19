# https://atcoder.jp/contests/abc225/tasks/abc225_a

S = input()
if len(set(S)) == 1:
    print(1)
elif len(set(S)) == 2:
    print(3)
else:
    print(6)
