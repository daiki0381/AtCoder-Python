# https://atcoder.jp/contests/abc276/tasks/abc276_c

N = int(input())
P = list(map(int, input().split()))

# ①Pの右からi項が単調増加となっている、最大のiを探しnとする。
n = N - 2
while P[n] < P[n + 1]:
    n -= 1

print(n)

# ②Pの右からn項の中でPの右からn項目の次に小さい数を探し、そのインデックスをmとする。
m = N - 1
while P[n] < P[m]:
    m -= 1

# ③Pの右からn項目とm項目目を交換し、右からn−1項を反転させる。
P[n], P[m] = P[m], P[n]
ans = P[: n + 1] + P[n + 1 :][::-1]
print(*ans)

# N = int(input())
# P = list(map(int, input().split()))

# n = N - 2
# is_increment = False

# # 減少パターン
# while P[n] > P[n + 1]:
#     n -= 1

# # 増加パターン
# while P[n] < P[n + 1]:
#     is_increment = True
#     n -= 1

# if is_increment:
#     m = N - 1
#     while P[n] < P[m]:
#         m -= 1
#     P[n], P[m] = P[m], P[n]

# ans = P[: n + 1] + P[n + 1 :][::-1]
# print(*ans)
