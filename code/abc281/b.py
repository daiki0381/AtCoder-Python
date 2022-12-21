# https://atcoder.jp/contests/abc281/tasks/abc281_b

S = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
zero_to_nine = "0123456789"
one_to_nine = "123456789"

if S[0] in alphabet and S[-1] in alphabet and len(S) == 8:
    if S[1] in one_to_nine and S[2] in zero_to_nine and S[3] in zero_to_nine and S[4] in zero_to_nine and S[5] in zero_to_nine and S[6] in zero_to_nine:
        print("Yes")
    else:
        print("No")
else:
    print("No")
