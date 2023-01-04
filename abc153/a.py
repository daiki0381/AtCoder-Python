# https://atcoder.jp/contests/abc153/tasks/abc153_a

H, A = map(int, input().split())
attack_num = 0
while H > 0:
    H -= A
    attack_num +=1
print(attack_num)
