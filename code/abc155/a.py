# https://atcoder.jp/contests/abc155/tasks/abc155_a

ABC = list(map(int, input().split()))
if len(set(ABC)) == 2:
    print("Yes")
else:
    print("No")
