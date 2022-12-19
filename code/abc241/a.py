# https://atcoder.jp/contests/abc241/tasks/abc241_a

a = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans = a[ans]
print(ans)
