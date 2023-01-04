# https://atcoder.jp/contests/abc229/tasks/abc229_b

A, B = map(int, input().split())

while A > 0 and B > 0:
    if (A % 10) + (B % 10) >= 10:
        print("Hard")
        break
    else:
        A //= 10
        B //= 10
else:
    print("Easy")
