# https://atcoder.jp/contests/abc208/tasks/abc208_b

import math

P = int(input())
ans = 0

while P != 0:
    if P - math.factorial(10) >= 0:
        P -= math.factorial(10)
        ans += 1
    elif P - math.factorial(9) >= 0:
        P -= math.factorial(9)
        ans += 1
    elif P - math.factorial(8) >= 0:
        P -= math.factorial(8)
        ans += 1
    elif P - math.factorial(7) >= 0:
        P -= math.factorial(7)
        ans += 1
    elif P - math.factorial(6) >= 0:
        P -= math.factorial(6)
        ans += 1
    elif P - math.factorial(5) >= 0:
        P -= math.factorial(5)
        ans += 1
    elif P - math.factorial(4) >= 0:
        P -= math.factorial(4)
        ans += 1
    elif P - math.factorial(3) >= 0:
        P -= math.factorial(3)
        ans += 1
    elif P - math.factorial(2) > ~0:
        P -= math.factorial(2)
        ans += 1
    elif P - math.factorial(1) >= 0:
        P -= math.factorial(1)
        ans += 1

print(ans)
