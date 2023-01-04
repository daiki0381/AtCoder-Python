# https://atcoder.jp/contests/abc247/tasks/abc247_b

N = int(input())
st_list = [input().split() for _ in range(N)]
is_satisfied = True

for st_index, st in enumerate(st_list):
    same_family_name = False
    same_last_name = False
    for col in range(N):
        for row in range(2):
            if st_index == col:
                continue
            else:
                if st[0] == st_list[col][row]:
                    same_family_name = True
                elif st[1] == st_list[col][row]:
                    same_last_name = True
    if same_family_name and same_last_name:
        is_satisfied = False

if is_satisfied:
    print("Yes")
else:
    print("No")
