# https://atcoder.jp/contests/abc203/tasks/abc203_b

def main():
    N, K = map(int, input().split())
    ans = 0
    for n in range(1, N + 1):
        for k in range(1, K + 1):
            ans += n * 100 + k

    print(ans)

if __name__ == "__main__":
    main()
