# https://atcoder.jp/contests/abc201/tasks/abc201_b

N = int(input())
ST = [input().split() for _ in range(N)]

print(sorted(ST, key=lambda x: int(x[1]))[-2][0])
