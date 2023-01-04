# https://atcoder.jp/contests/abc243/tasks/abc243_a

V, A, B, C = map(int, input().split())
if V % (A + B + C) == 0:
    print("F")
elif V < (A + B + C):
    if V - A < 0:
        print("F")
    elif V - A - B < 0:
        print("M")
    else:
        print("T")
else:
    if (V % (A + B + C)) - A < 0:
        print("F")
    elif (V % (A + B + C)) - A - B < 0:
        print("M")
    else:
        print("T")
