# https://atcoder.jp/contests/abc273/tasks/abc273_a

N = int(input())
def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)
print(f(N))
