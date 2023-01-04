# https://atcoder.jp/contests/abc260/tasks/abc260_a

S = input()
for i in range(3):
    if S.count(S[i]) == 1:
        print(S[i])
        break
else:
    print(-1)
