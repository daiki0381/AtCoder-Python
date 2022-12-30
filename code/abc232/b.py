# https://atcoder.jp/contests/abc232/tasks/abc232_b

S, T = [input() for _ in range(2)]

if ord(T[0]) - ord(S[0]) >= 0:
    common_num = ord(T[0]) - ord(S[0])
else:
    common_num = (ord(T[0]) - ord(S[0]) + 26) % 26

for i in range(len(S)):
    if ord(T[i]) - ord(S[i]) >= 0:
        if ord(T[i]) - ord(S[i]) != common_num:
            print("No")
            break
    else:
        if (ord(T[i]) - ord(S[i]) + 26) % 26 != common_num:
            print("No")
            break
else:
    print("Yes")
