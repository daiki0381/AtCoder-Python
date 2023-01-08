# https://atcoder.jp/contests/abc267/tasks/abc267_b

S = input()
col_list = [[S[6]], [S[3]], [S[1], S[7]], [S[0], S[4]], [S[2], S[8]], [S[5]], [S[9]]]

if S[0] == "0":
    if (
        col_list[1].count("0") == 1
        and col_list[0].count("1") != 0
        and (
            col_list[2].count("1") != 0
            or col_list[3].count("1") != 0
            or col_list[4].count("1") != 0
            or col_list[5].count("1") != 0
            or col_list[6].count("1") != 0
        )
    ):
        print("Yes")
    elif (
        col_list[2].count("0") == 2
        and (col_list[0].count("1") != 0 or col_list[1].count("1") != 0)
        and (
            col_list[3].count("1") != 0
            or col_list[4].count("1") != 0
            or col_list[5].count("1") != 0
            or col_list[6].count("1") != 0
        )
    ):
        print("Yes")
    elif (
        col_list[3].count("0") == 2
        and (
            col_list[0].count("1") != 0
            or col_list[1].count("1") != 0
            or col_list[2].count("1") != 0
        )
        and (
            col_list[4].count("1") != 0
            or col_list[5].count("1") != 0
            or col_list[6].count("1") != 0
        )
    ):
        print("Yes")
    elif (
        col_list[4].count("0") == 2
        and (
            col_list[0].count("1") != 0
            or col_list[1].count("1") != 0
            or col_list[2].count("1") != 0
            or col_list[3].count("1") != 0
        )
        and (col_list[5].count("1") != 0 or col_list[6].count("1") != 0)
    ):
        print("Yes")
    elif (
        col_list[5].count("0") == 1
        and (
            col_list[0].count("1") != 0
            or col_list[1].count("1") != 0
            or col_list[2].count("1") != 0
            or col_list[3].count("1") != 0
            or col_list[4].count("1") != 0
        )
        and (col_list[6].count("1") != 0)
    ):
        print("Yes")
    else:
        print("No")
else:
    print("No")
