# https://atcoder.jp/contests/abc244/tasks/abc244_b

N = int(input())
T = input()
direction = 0
x = 0
y = 0

for t in T:
    if t == "R":
        if direction != 3:
            direction += 1
        else:
            direction = 0
    else:
        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        else:
            y += 1

print(x, y)
