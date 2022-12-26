# https://atcoder.jp/contests/abc250/tasks/abc250_b

N, A, B = map(int, input().split())

for col_n in range(N):
    for col in range(A):
        for row_n in range(N):
            if col_n % 2 == 0 and row_n % 2 == 0 and row_n != N - 1:
                print("." * B, end="")
            elif col_n % 2 == 0 and row_n % 2 != 0 and row_n != N - 1:
                print("#" * B, end="")
            elif col_n % 2 != 0 and row_n % 2 == 0 and row_n != N - 1:
                print("#" * B, end="")
            elif col_n % 2 != 0 and row_n % 2 != 0 and row_n != N - 1:
                print("." * B, end="")
            if col_n % 2 == 0 and row_n % 2 == 0 and row_n == N - 1:
                print("." * B)
            elif col_n % 2 == 0 and row_n % 2 != 0 and row_n == N - 1:
                print("#" * B)
            elif col_n % 2 != 0 and row_n % 2 == 0 and row_n == N - 1:
                print("#" * B)
            elif col_n % 2 != 0 and row_n % 2 != 0 and row_n == N - 1:
                print("." * B)
