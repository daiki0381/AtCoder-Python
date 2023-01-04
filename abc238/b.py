# https://atcoder.jp/contests/abc238/tasks/abc238_b

# 切れ込みの位置を配列として格納する
# 現在の切れ込みの位置を0として初期化する

N = int(input())
A = list(map(int, input().split()))

positions = set()
current_angle = 0
positions.add(0)
positions.add(360)

for a in A:
    if current_angle + a >= 360:
        current_angle = current_angle + a - 360
        positions.add(current_angle)
    else:
        current_angle += a
        positions.add(current_angle)

angles = set()
for position_index, position in enumerate(sorted(positions)):
    if position_index != len(positions) - 1:
        angle = sorted(positions)[position_index + 1] - position
        angles.add(angle)

print(max(angles))
