# https://atcoder.jp/contests/abc213/tasks/abc213_b

N = int(input())
A = sorted(list(enumerate(list(map(int, input().split())))), key=lambda point: point[1])
print(A[-2][0] + 1)
