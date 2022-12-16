# https://atcoder.jp/contests/abc220/tasks/abc220_a

A, B, C = map(int, input().split())
while C <= 1000:
    if C >= A and C <= B:
        print(C)
        break
    C *= 2

if C > 1000:
    print(-1)
