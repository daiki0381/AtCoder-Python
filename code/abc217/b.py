# https://atcoder.jp/contests/abc217/tasks/abc217_b

S1 = input()
S2 = input()
S3 = input()
S = {S1, S2, S3}
all_contests = {"ABC", "ARC", "AGC", "AHC"}

print(*list((all_contests - S)))
