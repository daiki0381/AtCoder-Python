# https://atcoder.jp/contests/abc284/tasks/abc284_b

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for a in A:
        if a % 2 != 0:
            ans += 1
    print(ans)
