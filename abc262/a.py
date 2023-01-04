# https://atcoder.jp/contests/abc262/tasks/abc262_a

Y = int(input())
if Y % 4 == 2:
    print(Y)
else:
    while Y % 4 != 2:
        Y += 1
    print(Y)
