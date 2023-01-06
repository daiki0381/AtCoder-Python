# https://atcoder.jp/contests/abc274/tasks/abc274_c

N = int(input())
A = list(map(int, input().split()))
ans = [0] * (2 * N + 1)
for i, a in enumerate(A):
    # 親のアメーバに1を足す
    ans[2 * i + 1] = ans[a - 1] + 1
    ans[2 * i + 2] = ans[a - 1] + 1

print(*ans, sep="\n")
