# https://atcoder.jp/contests/abc228/tasks/abc228_a

S, T, X = map(int, input().split())
if S < T and S <= X < T:
    print("Yes")
elif S > T and (X < T or S <= X):
    print("Yes")
else:
    print("No")
