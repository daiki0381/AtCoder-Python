# https://atcoder.jp/contests/abc235/tasks/abc235_b

N = int(input())
H = list(map(int, input().split()))

ans = H[0]

for n in range(N):
    if n == 0:
        continue
    else:
        if ans < H[n]:
            ans = H[n]
        else:
            break

print(ans)
