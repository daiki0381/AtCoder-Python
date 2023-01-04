# https://atcoder.jp/contests/abc218/tasks/abc218_b

P = list(map(int, input().split()))

ans = ""

for p in P:
    num = 96 + p
    ans += chr(num)

print(ans)
