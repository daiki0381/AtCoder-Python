# https://atcoder.jp/contests/abc258/tasks/abc258_b

N = int(input())
A = [input() for _ in range(N)]
patterns = []
for row in range(N):
    for col in range(N):
        # 右移動
        right = A[row][col]
        right_extra_col_index = 0
        for n in range(1, N):
            if N - 1 < col + n:
                right += A[row][right_extra_col_index]
                right_extra_col_index += 1
            else:
                right += A[row][col + n]
        patterns.append(right)

        # 左移動
        left = A[row][col]
        left_extra_col_index = -1
        for n in range(1, N):
            if 0 > col - n:
                left += A[row][left_extra_col_index]
                left_extra_col_index -= 1
            else:
                left += A[row][col - n]
        patterns.append(left)

        # 上移動
        top = A[row][col]
        top_extra_row_index = -1
        for n in range(1, N):
            if 0 > row - n:
                top += A[top_extra_row_index][col]
                top_extra_row_index -= 1
            else:
                top += A[row - n][col]
        patterns.append(top)

        # 下移動
        bottom = A[row][col]
        bottom_extra_row_index = 0
        for n in range(1, N):
            if N - 1 < row + n:
                bottom += A[bottom_extra_row_index][col]
                bottom_extra_row_index += 1
            else:
                bottom += A[row + n][col]
        patterns.append(bottom)

        # 上右移動
        top_right = A[row][col]
        top_extra_row_index = -1
        right_extra_col_index = 0
        for n in range(1, N):
            if 0 > row - n and N - 1 < col + n:
                top_right += A[top_extra_row_index][right_extra_col_index]
                top_extra_row_index -= 1
                right_extra_col_index += 1
            elif 0 > row - n:
                top_right += A[top_extra_row_index][col + n]
                top_extra_row_index -= 1
            elif N - 1 < col + n:
                top_right += A[row - n][right_extra_col_index]
                right_extra_col_index += 1
            else:
                top_right += A[row - n][col + n]
        patterns.append(top_right)

        # 上左移動
        top_left = A[row][col]
        top_extra_row_index = -1
        left_extra_col_index = -1
        for n in range(1, N):
            if 0 > row - n and 0 > col - n:
                top_left += A[top_extra_row_index][left_extra_col_index]
                top_extra_row_index -= 1
                left_extra_col_index -= 1
            elif 0 > row - n:
                top_left += A[top_extra_row_index][col - n]
                top_extra_row_index -= 1
            elif 0 > col - n:
                top_left += A[row - n][left_extra_col_index]
                left_extra_col_index -= 1
            else:
                top_left += A[row - n][col - n]
        patterns.append(top_left)

        # 下右移動
        bottom_right = A[row][col]
        bottom_extra_row_index = 0
        right_extra_col_index = 0
        for n in range(1, N):
            if N - 1 < row + n and N - 1 < col + n:
                bottom_right += A[bottom_extra_row_index][right_extra_col_index]
                bottom_extra_row_index += 1
                right_extra_col_index += 1
            elif N - 1 < row + n:
                bottom_right += A[bottom_extra_row_index][col + n]
                bottom_extra_row_index += 1
            elif N - 1 < col + n:
                bottom_right += A[row + n][right_extra_col_index]
                right_extra_col_index += 1
            else:
                bottom_right += A[row + n][col + n]
        patterns.append(bottom_right)

        # 下左移動
        bottom_left = A[row][col]
        bottom_extra_row_index = 0
        left_extra_col_index = -1
        for n in range(1, N):
            if N - 1 < row + n and 0 > col - n:
                bottom_left += A[bottom_extra_row_index][left_extra_col_index]
                bottom_extra_row_index += 1
                left_extra_col_index -= 1
            elif N - 1 < row + n:
                bottom_left += A[bottom_extra_row_index][col - n]
                bottom_extra_row_index += 1
            elif 0 > col - n:
                bottom_left += A[row + n][left_extra_col_index]
                left_extra_col_index -= 1
            else:
                bottom_left += A[row + n][col - n]
        patterns.append(bottom_left)

print(max(patterns))
