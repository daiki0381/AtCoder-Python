# https://atcoder.jp/contests/abc248/tasks/abc248_a

# S = input()
# target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for s in S:
#     target.remove(int(s))
# print(int(*target))

S = input()
for i in range(10):
    if str(i) not in S:
        print(i)
        break
