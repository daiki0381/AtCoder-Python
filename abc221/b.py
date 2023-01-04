# https://atcoder.jp/contests/abc221/tasks/abc221_b

S = list(input())
T = list(input())

if S == T:
    print("Yes")
else:
    for i in range(len(S) - 1):
        new_s = S.copy()
        new_s[i] = S[i + 1]
        new_s[i + 1] = S[i]
        if new_s == T:
            print("Yes")
            break
    else:
        print("No")
