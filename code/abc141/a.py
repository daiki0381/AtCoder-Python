# https://atcoder.jp/contests/abc141/tasks/abc141_a

# weather = ["Sunny", "Cloudy", "Rainy"]
# S = input()
# if weather.index(S) != 2:
#     print(weather[weather.index(S) + 1])
# else:
#     print(weather[0])

weather = ["Sunny", "Cloudy", "Rainy", "Sunny"]
S = input()
print(weather[weather.index(S) + 1])
