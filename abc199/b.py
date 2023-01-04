# https://atcoder.jp/contests/abc199/tasks/abc199_b

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = []

for i in range(N):
    s = set()
    for j in range(A[i], B[i] + 1):
        s.add(j)
    AB.append(s)

current_set = AB[0]

for ab in AB:
    current_set = current_set & ab

print(len(current_set))
