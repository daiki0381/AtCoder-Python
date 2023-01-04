# https://atcoder.jp/contests/abc229/tasks/abc229_a

S1, S2 = [input() for _ in range(2)]
if S1[0] == "." and S1[1] == "#" and S2[0] == "#" and S2[1] == ".":
    print("No")
elif S1[0] == "#" and S1[1] == "." and S2[0] == "." and S2[1] == "#":
    print("No")
else:
    print("Yes")
