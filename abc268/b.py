# https://atcoder.jp/contests/abc268/tasks/abc268_b

S, T = [input() for _ in range(2)]

if len(S) > len(T):
    print("No")
else:
    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")
