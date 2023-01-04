# https://atcoder.jp/contests/abc281/tasks/abc281_c

N, T = map(int, input().split())
A = list(map(int, input().split()))

# ラスト1周の算出
T %= sum(A)

# ラスト1周で何番目か、何秒の時点か出力
for a_index, a in enumerate(A):
    if T - a < 0:
        print(a_index + 1, T)
        break
    else:
        T -= a
