# https://atcoder.jp/contests/abc175/tasks/abc175_a

S = input()
if S.count("R") == 0:
    print(0)
elif S.count("R") == 3:
    print(3)
elif S.count("R") == 1:
    print(1)
elif S.count("R") == 2:
    if S[1] == "S":
        print(1)
    else:
        print(2)
