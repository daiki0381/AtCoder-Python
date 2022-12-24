# https://atcoder.jp/contests/abc260/tasks/abc260_b

N, X, Y, Z = map(int, input().split())
success_list = []
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sorted_a = sorted(list(enumerate(A)), key=lambda x: x[1], reverse=True)
sorted_b = sorted(list(enumerate(B)), key=lambda x: x[1], reverse=True)

for x in range(X):
    success_list.append(sorted_a[x][0])

if len(success_list) != 0:
    for success in success_list:
        for b in sorted_b:
            if b[0] == success:
                sorted_b.remove(b)


for y in range(Y):
    success_list.append(sorted_b[y][0])

total_list = []

for n in range(N):
    total_list.append(A[n] + B[n])

total_list = sorted(list(enumerate(total_list)), key=lambda x: x[1], reverse=True)

if len(success_list) != 0:
    for success in success_list:
        for total in total_list:
            if total[0] == success:
                total_list.remove(total)

for z in range(Z):
    success_list.append(total_list[z][0])

for success in sorted(success_list):
    print(success + 1)
