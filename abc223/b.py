# https://atcoder.jp/contests/abc223/tasks/abc223_b

S = input()
ans_list = []

for _ in range(len(S)):
    ans_list.append(S)
    S = S[1:len(S)] + S[0]

print(min(ans_list))
print(max(ans_list))
