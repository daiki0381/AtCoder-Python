# https://atcoder.jp/contests/abc222/tasks/abc222_b

N, P = map(int, input().split())
points = list(map(int, input().split()))
ans = 0

for point in points:
    if P > point:
        ans += 1

print(ans)
