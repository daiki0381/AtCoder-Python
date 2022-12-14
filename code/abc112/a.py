# https://atcoder.jp/contests/abc112/tasks/abc112_a

N = int(input())
if N == 1:
    print("Hello World ")
else:
    A, B = [int(input()) for _ in range(2)]
    print(A + B)
