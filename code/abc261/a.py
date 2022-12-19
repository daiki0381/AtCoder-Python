# https://atcoder.jp/contests/abc261/tasks/abc261_a

L1, R1, L2, R2 = map(int, input().split())
L1_R1 = set()
L2_R2 = set()
for i in range(L1, R1 + 1):
    L1_R1.add(i)
for i in range(L2, R2 + 1):
    L2_R2.add(i)
if len(L1_R1 & L2_R2) == 0:
    print(0)
else:
    print(len(L1_R1 & L2_R2) - 1)
