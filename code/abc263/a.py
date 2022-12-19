# https://atcoder.jp/contests/abc263/tasks/abc263_a

ABCDE = list(sorted(map(int, input().split())))
if ABCDE[0] == ABCDE[1] == ABCDE[2] and ABCDE[2] != ABCDE[3] == ABCDE[4]:
    print("Yes")
elif ABCDE[0] == ABCDE[1] and ABCDE[1] != ABCDE[2] == ABCDE[3] == ABCDE[4]:
    print("Yes")
else:
    print("No")
