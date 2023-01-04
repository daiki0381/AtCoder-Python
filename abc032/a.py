# https://atcoder.jp/contests/abc032/tasks/abc032_a

a, b, n = [int(input()) for _ in range(3)]
for i in range (n, 100000):
  if i % a == 0 and i % b == 0:
    print(i)
    break
