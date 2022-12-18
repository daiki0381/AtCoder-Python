# https://atcoder.jp/contests/abc276/tasks/abc276_a

S = input()
if S.rfind("a") != -1:
    print(S.rfind("a") + 1)
else:
    print(-1)
