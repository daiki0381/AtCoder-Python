# https://atcoder.jp/contests/abc228/tasks/abc228_b

N, X = map(int, input().split())
A = list(map(int, input().split()))

secrets = [False] * N

while secrets[X - 1] == False:
    secrets[X - 1] = True
    X = A[X - 1]

print(secrets.count(True))
