# https://atcoder.jp/contests/abc056/tasks/abc056_a


a, b = input().split()
if a == "H" and b == "H":
    print("H")
elif a == "D" and b == "H":
    print("D")
elif a == "D" and b == "D":
    print("H")
else:
    print("D")
