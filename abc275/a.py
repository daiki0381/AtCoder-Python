# https://atcoder.jp/contests/abc275/tasks/abc275_a

N = int(input())
H = list(map(int, input().split()))
max = max(H)
print(H.index(max) + 1)
