# https://atcoder.jp/contests/abc272/tasks/abc272_c

# 2要素の和が偶数になるのは、偶数と偶数を足したときか奇数と奇数を足したとき

N = int(input())
A = list(map(int, input().split()))
odds = []
evens = []

for a in A:
    if a % 2 == 0:
        evens.append(a)
    else:
        odds.append(a)

if len(odds) < 2 and len(evens) < 2:
    print(-1)
    exit()

odds.sort()
evens.sort()

if len(odds) >= 2 and len(evens) >= 2:
    odds_max = odds[-1] + odds[-2]
    evens_max = evens[-1] + evens[-2]
    if odds_max > evens_max:
        print(odds_max)
    else:
        print(evens_max)
elif len(odds) >= 2:
    print(odds[-1] + odds[-2])
else:
    print(evens[-1] + evens[-2])
