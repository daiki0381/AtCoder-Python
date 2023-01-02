# https://atcoder.jp/contests/abc198/tasks/abc198_b

N = input()

for i in range(1000):
    if "0" * i + N == ("0" * i + N)[::-1]:
        print("Yes")
        break
else:
    print("No")
