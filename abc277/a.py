# https://atcoder.jp/contests/abc277/tasks/abc277_a

N, X = map(int, input().split())
l = map(int, input().split())
k = 1
for i in l:
    if i == X:
        break
    k += 1
print(k)
