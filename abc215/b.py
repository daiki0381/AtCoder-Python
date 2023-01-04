# https://atcoder.jp/contests/abc215/tasks/abc215_b

N = int(input())

ans = 0

while 2**ans <= N:
    ans += 1

print(ans - 1)
