# https://atcoder.jp/contests/abc249/tasks/abc249_b

S = input()
is_lower = False
is_upper = False
is_same = True

for s in S:
    if s.isupper():
        is_upper = True
    if s.islower():
        is_lower = True
    if S.count(s) != 1:
        is_same = False

if is_lower and is_upper and is_same:
    print("Yes")
else:
    print("No")
