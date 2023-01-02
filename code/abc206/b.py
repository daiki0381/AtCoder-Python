# https://atcoder.jp/contests/abc206/tasks/abc206_b

def main():
    N = int(input())
    ans = 0

    for i in range(1, 10**5):
        N -= i
        ans += 1
        if N <= 0:
            print(ans)
            break

if __name__ == "__main__":
    main()
