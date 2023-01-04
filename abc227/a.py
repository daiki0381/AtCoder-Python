# https://atcoder.jp/contests/abc227/tasks/abc227_a

def main():
    N, K, A = map(int, input().split())
    current_num = A

    for i in range(K):
        if i == 0:
            continue
        else:
            if current_num == N:
                current_num = 1
                continue
            current_num += 1

    print(current_num)

if __name__ == "__main__":
    main()
