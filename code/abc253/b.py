# https://atcoder.jp/contests/abc253/tasks/abc253_b

H, W = map(int, input().split())
S = [input() for _ in range(H)]

positions = []

for i, s in enumerate(S):
    if s.count("o") == 1:
        x = i
        y = s.find("o")
        positions.append((x, y))
    elif s.count("o") == 2:
        x = i
        y_1 = s.find("o")
        y_2 = s.rfind("o")
        positions.append((x, y_1))
        positions.append((x, y_2))

print(abs(positions[0][0] - positions[1][0]) + abs(positions[0][1] - positions[1][1]))
