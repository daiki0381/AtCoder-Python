# https://atcoder.jp/contests/abc088/tasks/abc088_a

N, A = [int(input()) for _ in range(2)]
if N % 500 <= A:
    print("Yes")
else:
    print("No")
