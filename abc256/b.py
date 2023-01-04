# https://atcoder.jp/contests/abc256/tasks/abc256_b

N = int(input())
A = map(int, input().split())
runners = []
P = 0

for a in A:
    runners.append(0)
    for runner_index in range(len(runners)):
        runners[runner_index] = runners[runner_index] + a

for runner in runners:
    if runner >= 4:
        P += 1
print(P)
