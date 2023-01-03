# https://atcoder.jp/contests/abc192/tasks/abc192_b

S = input()

for s_index, s in enumerate(S):
    if (s_index + 1) % 2 == 0:
        if not s.isupper():
            print("No")
            break
    else:
        if not s.islower():
            print("No")
            break
else:
    print("Yes")
