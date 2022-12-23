# https://atcoder.jp/contests/abc269/tasks/abc269_b

S = [input() for _ in range(10)]
containing_row_list = []
for i in range(10):
    if S[i].count("#") != 0:
        containing_row_list.append(i + 1)
print(min(containing_row_list), max(containing_row_list))
print(
    S[containing_row_list[0] - 1].find("#") + 1,
    S[containing_row_list[0] - 1].rfind("#") + 1,
)
