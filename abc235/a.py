# https://atcoder.jp/contests/abc235/tasks/abc235_a

a, b, c = input()
print(int(a + b + c) + int(b + c + a) + int(c + a + b))
