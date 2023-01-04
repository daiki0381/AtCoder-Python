# https://atcoder.jp/contests/abc028/tasks/abc028_a

N = int(input())
if N <= 59:
    print("Bad")
elif N >= 60 and N <= 89:
    print("Good")
elif N >= 90 and N <= 99:
    print("Great")
else:
    print("Perfect")
