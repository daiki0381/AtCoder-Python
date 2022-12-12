# https://atcoder.jp/contests/abc017/tasks/abc017_1

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())
print((s1 * e1 // 10) + (s2 * e2 // 10) + (s3 * e3 // 10))
