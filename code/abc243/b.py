# https://atcoder.jp/contests/abc243/tasks/abc243_b

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

same_position_num = 0
different_position_num = 0

for a_i ,a in enumerate(A):
    for b_i, b in enumerate(B):
        if a == b and a_i == b_i:
            same_position_num += 1
        elif a == b:
            different_position_num += 1

print(same_position_num)
print(different_position_num)
