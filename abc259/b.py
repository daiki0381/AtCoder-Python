# https://atcoder.jp/contests/abc259/tasks/abc259_b

a, b, d = map(int, input().split())

import math

d_rad = math.radians(d)

a_rotated = a * math.cos(d_rad) - b * math.sin(d_rad)
b_rotated = a * math.sin(d_rad) + b * math.cos(d_rad)

print(a_rotated, b_rotated)
