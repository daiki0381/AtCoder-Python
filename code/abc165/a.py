# https://atcoder.jp/contests/abc165/tasks/abc165_a

# K = int(input())
# A, B = map(int, input().split())
# for i in range(1, 1001):
#     if i % K == 0 and A <= i <= B:
#         print("OK")
#         break
# else:
#     print("NG")

K = int(input())
A, B = map(int, input().split())
for i in range(A, B + 1):
    if i % K == 0:
        print("OK")
        break
else:
    print("NG")
