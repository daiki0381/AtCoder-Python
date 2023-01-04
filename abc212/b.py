# https://atcoder.jp/contests/abc212/tasks/abc212_b

X = input()

if X[0] == X[1] == X[2] == X[3]:
    print("Weak")
    exit()

current_num = int(X[0])

for i in range(1, 4):
    if current_num == 9 and int(X[i]) != 0:
        print("Strong")
        break
    elif current_num != 9 and int(X[i]) != current_num + 1:
        print("Strong")
        break
    current_num = int(X[i])
else:
    print("Weak")
