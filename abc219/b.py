# https://atcoder.jp/contests/abc219/tasks/abc219_b

S1, S2, S3, T = [input() for _ in range(4)]

ans = ""

for t in T:
    if t == "1":
        ans += S1
    elif t == "2":
        ans += S2
    else:
        ans += S3
print(ans)
