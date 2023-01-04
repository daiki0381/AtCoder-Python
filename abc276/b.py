# https://atcoder.jp/contests/abc276/tasks/abc276_b

N, M = map(int, input().split())
nested_cities = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    nested_cities[A - 1].append(B)
    nested_cities[B - 1].append(A)
for cities in nested_cities:
    print(len(cities), *sorted(cities))
