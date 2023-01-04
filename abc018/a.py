# https://atcoder.jp/contests/abc018/tasks/abc018_1

taro_point, jiro_point, saburo_point = [int(input()) for _ in range(3)]
sorted_point = sorted([taro_point, jiro_point, saburo_point])[::-1]
print(sorted_point.index(taro_point) + 1)
print(sorted_point.index(jiro_point) + 1)
print(sorted_point.index(saburo_point) + 1)
