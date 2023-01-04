# https://atcoder.jp/contests/abc211/tasks/abc211_b

S = [input() for _ in range(4)]

if (
    S.count("H") == 1
    and S.count("2B") == 1
    and S.count("3B") == 1
    and S.count("HR") == 1
):
    print("Yes")
else:
    print("No")
