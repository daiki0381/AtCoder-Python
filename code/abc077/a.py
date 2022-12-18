# https://atcoder.jp/contests/abc077/tasks/abc077_a

C1, C2 = [input() for _ in range(2)]
if C1 == C2[::-1]:
    print("YES")
else:
    print("NO")
